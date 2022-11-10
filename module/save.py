from module.setting import instCpCybos
from module.get import get_stock_info
from module.search import search_by_code
from module.update import update_stock_list

from tqdm import tqdm
from datetime import datetime
from datetime import timedelta
import pandas as pd
import os
import time


# 전체 일자 분봉 종목 데이터 가져와서 csv 파일로 저장
def save_stock_info_auto(stock_code, end_day, type):
    
    day_format = '%Y%m%d'
    minus_day = timedelta(days=1)
    
    stock_df = get_stock_info(stock_code, end_day, end_day, type) # 첫번째 DF 생성 => pre_day '20221028' end_day '20221103'
    
    stock_name = search_by_code(stock_code)

    for day in range(740): # range 범위 수정하지 말 것
        transfer_pre_day = datetime.strptime(end_day, day_format) # '20221028' '20221023'
        pre_day = datetime.strftime(transfer_pre_day - minus_day, day_format) # '20221023' '20221018'

        info_second = get_stock_info(stock_code, pre_day, pre_day, type) # '20221023' '20221027'

        time.sleep(0.15)
        end_day = pre_day
        print(pre_day)

        stock_df = pd.concat([stock_df, info_second], axis=0)
        info_second = pd.DataFrame()
        print(stock_df.shape)
        print(stock_name, 'Count : {0}, 남은 요청 횟수 :{1}'.format(day, instCpCybos.GetLimitRemainCount(1)))
        
        if  instCpCybos.GetLimitRemainCount(1) < 5:
            time.sleep(10)
    
    stock_df.to_csv(r'\\DESKTOP-H2H6JNB\data\data\{0}_{1}.csv'.format(stock_name[0][1:],stock_name[1]), encoding='utf-8-sig')

    return stock_df


# 전체 일자 분봉 종목 데이터 가져와서 csv 파일로 저장
def save_stock_info_auto(stock_code, end_day, type):
    
    day_format = '%Y%m%d'
    minus_day = timedelta(days=1)
    
    stock_df = get_stock_info(stock_code, end_day, end_day, type) # 첫번째 DF 생성 => pre_day '20221028' end_day '20221103'
    
    stock_name = search_by_code(stock_code)

    for day in range(740): # range 범위 수정하지 말 것
        transfer_pre_day = datetime.strptime(end_day, day_format) # '20221028' '20221023'
        pre_day = datetime.strftime(transfer_pre_day - minus_day, day_format) # '20221023' '20221018'

        info_second = get_stock_info(stock_code, pre_day, pre_day, type) # '20221023' '20221027'

        time.sleep(0.15)
        end_day = pre_day
        print(pre_day)

        stock_df = pd.concat([stock_df, info_second], axis=0)
        info_second = pd.DataFrame()
        print(stock_df.shape)
        print(stock_name, 'Count : {0}, 남은 요청 횟수 :{1}'.format(day, instCpCybos.GetLimitRemainCount(1)))
        
        if  instCpCybos.GetLimitRemainCount(1) < 5:
            time.sleep(10)
    
    stock_df.to_csv(r'\\DESKTOP-H2H6JNB\data\data\{0}_{1}.csv'.format(stock_name[0][1:],stock_name[1]), encoding='utf-8-sig')

    return stock_df


# 리스트 수정본 저장
def save_stock_list_real(n, code, end_day, type):
    for code in update_stock_list()[n:]:
        save_stock_info_auto(code, end_day, type)


# 분봉과 일봉 사이에 이름이 일치하는 것만 가져오기
def choice_stock_same():

    files_m = os.listdir('../data')
    files_d = os.listdir('../day_data') 

    for min_df, day_df in tqdm(zip(files_m, files_d)):
        stock_min = pd.read_csv(f'../data/{min_df}', index_col='Unnamed: 0')
        stock_day = pd.read_csv(f'../data_day/{day_df}', index_col='Unnamed: 0')
        
        if min_df.split('_')[-2] == day_df.split('_')[-2]:
            stock_min.to_csv(f'../stock_min/{min_df}')
            stock_day.to_csv(f'../stock_day/{day_df}')
            
        

# 분봉 일봉 합쳐서 저장
def save_min_day_concat():
    # 파일 불러오기
    files_min = os.listdir('../data/stock_min')
    files_day = os.listdir('../data/stock_day') 
    
    # 파일 정렬하기
    files_min.sort()
    files_day.sort()
    
    for min_df, day_df in tqdm(zip(files_min, files_day)):
        stock_min_df = pd.read_csv(f'../data/stock_min/{min_df}', index_col='Unnamed: 0')
        stock_day_df = pd.read_csv(f'../data/stock_day/{day_df}', index_col='Unnamed: 0')
        
    
        concat_list = []
        concat_list.append('A' + files_min[j].split('_')[-2])
        
        for v in stock_min_df.index:
            input_list = ['전일대비','상장주식수','시가총액','외국인주문한도수량'
                    ,'외국인주문가능수량','외국인현보유수량','외국인현보유비율'
                    ,'수정주가일자','수정주가비율','기관순매수량','기관누적순매수량']
            
            stock_min_df.loc[v, input_list] = stock_day_df.loc[v, input_list].values
        for code in concat_list:        
            stock_min_df.to_csv('../data/concat_data/concat_{0}_{1}.csv'.format(
                            search_by_code(code)[0][1:],search_by_code(code)[1]
                            ), encoding='utf-8-sig') 
            
            
def save_label_stock_info():

    files_list = os.listdir('../data/concat_data/')
    
    for file_name in files_list:

        stock_info = pd.read_csv(f'../data/concat_data/{file_name}', index_col=0)
        
        concat_list =  []
        concat_list.append('A' + file_name.split('_')[-2])

        # for문 1 => 날짜를 반복
        date = stock_info.index.unique()
        stock_info['label'] = 0

        update_stock_info = pd.DataFrame()

        for day in tqdm(date):
            select_day = stock_info.loc[day].copy() # 특정일
            select_day['label'] = 0
            
            # for i in range(len(select_day)):
            for row in range(len(select_day)):
            # for문 2 => 시간을 반복
                pre_price = select_day.iloc[-row-1].values[2] # 선택된 분봉(ROW)의 고가를 가져온다
                # for i in range(len(select_day)-i):
                # print('인덱스 : {0}, 분봉 시간 : {1}'.format(row,select_day.iloc[-row-1].values[0]))
                # print('해당 분봉의 고가 : {0}'.format(pre_price))
                next_price = select_day[-row-1::-1]['고가'].max()
                # print('이후 최대 고가 : {0}'.format(next_price))
                select_day.iloc[-row-1,-1] = next_price
                next_price = 0
            
            update_stock_info = pd.concat([update_stock_info,select_day])
        for code in concat_list:
            update_stock_info.to_csv('../data/label/label_{0}_{1}.csv'.format(
                search_by_code(code)[0][1:],search_by_code(code)[1]
                ), encoding='utf-8-sig')