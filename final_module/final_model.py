from tensorflow.keras.layers import Input, BatchNormalization, Activation
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.models import Model
from tensorflow.keras import optimizers

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MaxAbsScaler

from final_module.final_dbconnect import DBConnection

from pandas.tseries.offsets import BDay
from keras.models import load_model
from datetime import date
from pickle import dump
from tqdm import tqdm

import pandas as pd
import numpy as np
import pickle
import glob
import os


class DBNetwork(DBConnection):
    def __init__(self, stock_type, stock_table_list, period, day, corr
                 , today =str(date.today()).replace('-',''), yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0],*args, **kwargs):
        super().__init__(*args, **kwargs)
        super().get_pymysql_connection()
        super().get_sqlalchemy_connect_ip()
        self.today = today
        self.yesterday = yesterday
        self.result = None
        self.empty_day_df = None
        self.investing_df = None
        self.stock_type = stock_type
        self.stock_table_list = stock_table_list
        self.period = period
        self.period_day = str(date.today() - BDay(day)).replace('-','').split(' ')[0]
        self.corr = corr
    
    #DB 내 존재하는 테이블(종목) 리스트 추출
    def get_pymysql_stock_list(self):
        # 원하는 폴더의 테이블(종목) 추출
        sql = f"SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{self.db_name}'"

        with self.py_con:
            with self.py_con.cursor() as cur:
                cur.execute(sql)
                result = [item[0] for item in cur.fetchall()]
                cur.close()
                self.result = result
                return result

     # 병합을 위해 날짜만을 가지고 있는 데이터 프레임 생성
    def get_empty_day_df(self):
        
        sql = f"SELECT * FROM investing_data.코스피지수내역 where 날짜 >= {self.period_day} and 날짜 <= {self.yesterday}"    
        table_data = self.sq_con.execute(sql) 
        table_df = pd.DataFrame(table_data.fetchall())  # DB내 테이블을 DF로 변환
        table_df['날짜'] = pd.to_numeric(table_df['날짜'])
        empty_day_df = table_df.drop(columns=['코스피지수내역_종가','코스피지수내역_오픈','코스피지수내역_고가'
                                        ,'코스피지수내역_저가','코스피지수내역_거래량','코스피지수내역_변동']) # 날짜를 제외한 컬럼 drop
        
        empty_day_df.to_pickle(f'./pickle/pickle_df/empty/{self.yesterday}_{self.period}.pkl')
        
        self.empty_day_df = empty_day_df
        return empty_day_df
    # investing Data로 이루어진 데이터 프레임 추출
    def get_sqlalchemy_investing_df(self):
        
        investing_df = self.empty_day_df
        for table in self.result:
            
            sql = f"SELECT * FROM investing_data.`{table}` where 날짜 >= {self.period_day} and 날짜 <= {self.today}"
            table_data= self.sq_con.execute(sql)
            table_df = pd.DataFrame(table_data.fetchall())  # DB내 테이블을 DF로 변환
            table_df['날짜'] =pd.to_numeric(table_df['날짜'])
            table_df.drop_duplicates(subset='날짜', inplace=True)
            investing_df = pd.merge(investing_df, table_df,on='날짜', how='left') # investing data들을 하나의 df로 제작
            
        # 빈 값 채워주기    
        for c in list(investing_df.columns):
            if c.split('_')[-1] == '거래량' or c.split('_')[-1] == '변동':
                investing_df[c] = investing_df[c].fillna(0)
            else:
                investing_df[c] = investing_df[c].fillna(method='bfill')
                investing_df[c] = investing_df[c].fillna(method='ffill')
                
        investing_df.to_pickle(f'./pickle/pickle_df/investing/{self.today}_{self.period}_10개.pkl')
    
        self.investing_df = investing_df 
        return investing_df


class DataFrameCreate(DBNetwork):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        super().get_pymysql_stock_list()
        super().get_empty_day_df()
        super().get_sqlalchemy_investing_df()
        self.complete_df = None
        self.complete_corr = None
        
    # stock df와 investing df를 병합
    def get_sqlalchemy_stock_investing_merge_df(self):
        
        investing_df = self.investing_df
        
        complete_df = pd.DataFrame()
        for table in tqdm(self.stock_table_list):
            sql = f"SELECT * FROM stock_info.`{table}` where 날짜 >= {self.period_day} and 날짜 <= {self.today}"
            table_data = self.sq_con.execute(sql)
            stock_df = pd.DataFrame(table_data.fetchall()) # DB내 테이블을 DF로 변환
            stock_df['날짜'] = pd.to_numeric(stock_df['날짜'])
            drop_list = ['외국인주문한도수량','외국인주문가능수량','수정주가일자','수정주가비율']
            stock_df.drop(drop_list,axis=1, inplace=True)
            
            merge_df = pd.merge(stock_df, investing_df, on='날짜') # stock df 와 investing df 를 날짜 기준으로 merge
            
            
            complete_df = pd.concat([complete_df, merge_df], axis=0) # merge가 된 df들을 concat하여 하나의 df로 제작
        
        day_col_list = ['전일대비','상장주식수','시가총액','외국인현보유수량'
                        ,'외국인현보유비율','기관순매수량','기관누적순매수량'
                        , '년', '월', '일']   
        investing_col_list= list(investing_df.columns.drop('날짜'))

        shift_list = day_col_list + investing_col_list

        for col in shift_list:
            complete_df[col] = complete_df[col].shift(381)
        complete_df.dropna(inplace=True)
        
        # 폴더가 없을 경우 생성
        if not os.path.isdir('../data/pickle_complete'):
            os.makedirs('../data/pickle_complete')

        complete_df.to_pickle(f'../data/pickle_complete/{self.stock_type}_{self.today}_{self.period}_10개.pkl')
        print('학습 모델 저장 완료')
        self.sq_con.close()
        self.complete_df = complete_df
        return complete_df
  
    def get_corr_list(self):

        target = "./pickle/pickle_corr_matrix/*.pkl"
        pkl_list = glob.glob(target)
        check = False
        if len(pkl_list) >= 1: # 파일이 있는 경우
    
            for i in range(len(pkl_list)):

                stock_type = pkl_list[i].split('\\')[-1].split('_')[0] # 소형주
                stock_day = pkl_list[i].split('\\')[-1].split('_')[1] # 오늘
                stock_period = pkl_list[i].split('\\')[-1].split('_')[2] # 6개월
                
                # 파일은 있는데 날짜가 일치하지 않는 경우
                if (stock_type == self.stock_type) and (stock_day == self.today) and (stock_period == self.period):
                    check = True

            # True일 경우 파일이 존재하므로 기존 데이터 로드
            if check == True:
                stock_df = self.complete_df
                with open( f'./pickle/pickle_corr_matrix/{self.stock_type}_{self.today}_{self.period}_10개.pkl', 'rb') as p:
                    corr_matrix = pickle.load(p)

            # 파일이 없는 경우 새로 생성
            else:
                stock_df = self.complete_df
                corr_matrix = stock_df.corr()
                corr_matrix.to_pickle(f'./pickle/pickle_corr_matrix/{self.stock_type}_{self.today}_{self.period}_10개.pkl')
                print('상관계수 저장 완료')

        # 폴더 내 파일이 없는 경우
        else: 
            stock_df = self.complete_df
            corr_matrix = stock_df.corr()
            corr_matrix.to_pickle(f'./pickle/pickle_corr_matrix/{self.stock_type}_{self.today}_{self.period}_10개.pkl')
            print('상관계수 저장 완료')
        
        # 상관 계수가 낮은 경우 drop
        drop_list = []
        for i, cor in tqdm(enumerate(corr_matrix.columns)):
            for v, j in zip(corr_matrix.loc[cor].values, corr_matrix.iloc[i].index ):
                # print(v)
                if (v > 0.8) & (v!=1) & (j not in drop_list):
                    drop_list.append(j)
                
        cor_list = list(corr_matrix.columns)
        for i in tqdm(drop_list):
            cor_list.remove(i)
        
        # 필수 컬럼이 빠진 경우 추가
        essential_list = ['날짜','시간','시가','고가','저가','종가','거래량','거래대금','누적체결매도수량','누적체결매수수량','년','월','일']
        for e in tqdm(essential_list):
            if e not in cor_list: 
                cor_list.append(e)

        # 1차 필터된 리스트에서 pct_label과 상관계수 재추출
        corr_df = stock_df[cor_list].corr()
        new_corr = corr_df["pct_label"]
        new_corr.to_pickle(f'./pickle/pickle_corr_complete/{self.stock_type}_{self.today}_{self.period}_10개.pkl')   

        # 날짜 년, 월, 일 별도로 추출하므로 drop
        new_corr= new_corr.drop('날짜')
        complete_corr = new_corr[(new_corr.values>self.corr) | (new_corr.values<-self.corr) |
                        (new_corr.index == '시간') | (new_corr.index == '시가') | (new_corr.index == '고가') | (new_corr.index == '저가') | 
                        (new_corr.index == '종가') | (new_corr.index == '거래량') | (new_corr.index == '거래대금') | 
                        (new_corr.index == '누적체결매도수량') | (new_corr.index == '누적체결매수수량') | 
                        (new_corr.index == '년') | (new_corr.index == '월') | (new_corr.index == '일')]
        complete_corr = complete_corr.drop('pct_label')
        complete_corr.to_pickle(f'./pickle/pickle_corr_complete/{self.stock_type}_{self.today}_{self.period}_10개_{self.corr}.pkl')
        self.complete_corr = complete_corr

        return complete_corr

    
class LstmNetwork(DataFrameCreate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.epochs = 30
        self.patience = 5
        self.batch_size = 64
        self.learning_rate = 0.001
        self.decay = 1e-7
        self.col_list = None
        self.model_weight = None

        # 생성된 모델이 있는지 확인
        target = "./model/weight/*.hdf5"
        model_list = glob.glob(target)
        check = False
        for md in model_list:
            md = md.split('\\')[-1]
            if md == f'{self.stock_type}_{self.today}_{self.period}_lstm_{self.epochs}ep_{self.batch_size}bs_{self.patience}pa_{self.corr}newcor.hdf5':
                check = True
        print(check)

        # 모델이 없는 경우 lstm_model()로 진입하여 모델 생성
        if check == False:
            self.lstm_model()

        # 모델이 있는 경우 상관계수 로드
        else:
            with open(f'./pickle/pickle_corr_complete//{self.stock_type}_{self.today}_{self.period}_10개_{self.corr}.pkl', 'rb') as f:
                col_list = pickle.load(f) # 상관 계수에 따른 컬럼 리스트
            model_weight = load_model(f"./model/weight/{self.stock_type}_{self.today}_{self.period}_lstm_{self.epochs}ep_{self.batch_size}bs_{self.patience}pa_{self.corr}newcor.hdf5")
            self.col_list =col_list
            self.model_weight = model_weight
        

    def lstm_model(self):
        super().get_sqlalchemy_stock_investing_merge_df()
        super().get_corr_list()
        stock_df = self.complete_df
        with open(f'./pickle/pickle_corr_complete//{self.stock_type}_{self.today}_{self.period}_10개_{self.corr}.pkl', 'rb') as f:
            col_list = pickle.load(f) # 상관 계수에 따른 컬럼 리스트

        if '날짜' in col_list:
            col_list= col_list.drop('날짜')   

        stock_df['pct_label'] = np.where(stock_df['pct_label'].values > 0.5 , 1, 0)

        # label 원 핫 인코딩
        ohe = OneHotEncoder(sparse=False)
        y_stock_df = ohe.fit_transform(stock_df[['pct_label']])

        # value 컬럼 설정
        col_list = list(col_list.index) # col_list의 인덱스를 리스트로 생성
        X_stock_df = stock_df.drop(['pct_label'],axis=1)
        X_stock_df = X_stock_df.set_index(['날짜'])
        X_stock_df = X_stock_df[col_list] # col_list에 있는 컬럼들만 사용

        min_abs_scaler = MaxAbsScaler()
        X_stock_sc = min_abs_scaler.fit_transform(X_stock_df)
        dump(min_abs_scaler, open(f'./download/scaler/{self.today}_scaler', 'wb'))
        X_train, X_test, y_train, y_test = train_test_split(X_stock_sc, y_stock_df
                                                            , test_size=0.3, shuffle=True
                                                            , random_state=42, stratify=y_stock_df)

        X_train = X_train.reshape(X_train.shape[0], X_stock_df.shape[1], 1)
        X_test = X_test.reshape(X_test.shape[0], X_stock_df.shape[1], 1)

        # 모델 설정
        inputs = Input(shape=(X_stock_df.shape[1],1))
        lstm_out = LSTM(16, dropout=0.2,return_sequences=True)(inputs)
        lstm_out = BatchNormalization()(lstm_out)
        lstm_out = Activation('PReLU')(lstm_out)
        lstm_out = LSTM(16, dropout=0.2)(lstm_out)
        lstm_out = BatchNormalization()(lstm_out)
        lstm_out = Activation('PReLU')(lstm_out)
        lstm_out = Dense(2)(lstm_out)
        lstm_out = BatchNormalization()(lstm_out)
        lstm_out = Activation('softmax')(lstm_out) 

        # stop지점 설정
        early_stopping_callback = EarlyStopping(monitor='val_loss', patience=self.patience)

        # 모델 이름 설정
        modelpath=f"./model/weight/{self.stock_type}_{self.today}_{self.period}_lstm_{self.epochs}ep_{self.batch_size}bs_{self.patience}pa_{self.corr}newcor.hdf5"
        # 최적화 모델을 업데이트하고 저장합니다.
        checkpointer = ModelCheckpoint(filepath=modelpath, monitor='val_loss', verbose=0, save_best_only=True)

        model = Model(inputs=inputs, outputs=lstm_out)
        model.summary()
        model.compile(loss='categorical_crossentropy', optimizer=optimizers.Adam(learning_rate=self.learning_rate, decay=self.decay), metrics=['accuracy'])

        history=model.fit(X_train, y_train, epochs=self.epochs, batch_size=self.batch_size,verbose=1, validation_data=(X_test, y_test), callbacks=[early_stopping_callback, checkpointer])

        with open(f'./model/history/{self.stock_type}_{self.today}_{self.period}_lstm_{self.epochs}ep_{self.batch_size}bs_{self.patience}pa_{self.corr}newcor.json', 'wb') as f:
            pickle.dump(history.history, f)
           
        model_weight = load_model(f"./model/weight/{self.stock_type}_{self.today}_{self.period}_lstm_{self.epochs}ep_{self.batch_size}bs_{self.patience}pa_{self.corr}newcor.hdf5")
        self.col_list = col_list
        self.model_weight = model_weight
        return col_list, model_weight