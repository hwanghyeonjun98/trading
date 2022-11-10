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
    files_m = os.listdir('../data/data')
    files_d = os.listdir('../data/day_data') 

    for min_df in tqdm(files_m):
        for day_df in files_d:
            stock_min = pd.read_csv(f'../data/data/{min_df}', index_col='Unnamed: 0')
            stock_day = pd.read_csv(f'../data/day_data/{day_df}', index_col='Unnamed: 0')
            
            if min_df.split('_')[-2] == day_df.split('_')[-2]:
                stock_min.to_csv(f'../data/stock_min/{min_df}')
                stock_day.to_csv(f'../data/stock_day/{day_df}')
            
        

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
        concat_list.append('A' + files_min.split('_')[-2])
         
        for v in stock_min_df.index:
            input_list = ['전일대비','상장주식수','시가총액','외국인주문한도수량'
                    ,'외국인주문가능수량','외국인현보유수량','외국인현보유비율'
                    ,'수정주가일자','수정주가비율','기관순매수량','기관누적순매수량']
            
            stock_min_df.loc[v, input_list] = stock_day_df.loc[v, input_list].values
        for code in concat_list:        
            stock_min_df.to_csv('../data/concat_data/concat_{0}_{1}.csv'.format(
                            search_by_code(code)[0][1:],search_by_code(code)[1]
                            ), encoding='utf-8-sig') 
            
            
# Concat 완료된 데이터 Labeling 추가
def save_label_stock_info():

    # Concat 데이터 불러오기
    files_list = os.listdir('../data/concat_data/')
    
    for file_name in tqdm(files_list):

        stock_info = pd.read_csv(f'../data/concat_data/{file_name}', index_col=0)
        
        concat_list =  []
        concat_list.append('A' + file_name.split('_')[-2])

        # 데이터 프레임에서 날짜 인덱스 추출
        date = stock_info.index.unique()

        # label 컬럼 추가 후 0으로 초기화
        stock_info['label'] = 0

        # 업데이트에 사용할 데이터 프레임 생성
        update_stock_info = pd.DataFrame()

        # labeling
        for day in date:

            # 특정일의 Data 추출
            select_day = stock_info.loc[day].copy()
            select_day['label'] = 0
            
            # 특정일의 Row 만큼 반복
            for row in range(len(select_day)):
                
                # 특정일의 현재 row 이후 최대 고가를 추출
                next_price = select_day[-row-1::-1]['고가'].max()

                # 추출한 최대 고가를 label 컬럼에 대입
                select_day.iloc[-row-1,-1] = next_price
                next_price = 0
            
            # 특정일 label이 추가된 DF를 업데이트할 DF에 concat
            update_stock_info = pd.concat([update_stock_info, select_day])
        
        # 업데이트된 DF 저장
        for code in concat_list:
            update_stock_info.to_csv('../data/label/label_{0}_{1}.csv'.format(
                search_by_code(code)[0][1:],search_by_code(code)[1]
                ), encoding='utf-8-sig')

####################################################################################
# Modeling 테스트용 label 함수 => 삭제 예정
####################################################################################
def test_save_label_stock_info():

    # Concat 데이터 불러오기
    files_list = os.listdir('../data/test/')
    
    for file_name in tqdm(files_list):

        stock_info = pd.read_csv(f'../data/test/{file_name}', index_col=0)
        
        concat_list =  []
        concat_list.append('A' + file_name.split('_')[-2])

        # 데이터 프레임에서 날짜 인덱스 추출
        date = stock_info.index.unique()

        # label 컬럼 추가 후 0으로 초기화
        stock_info['label'] = 0

        # 업데이트에 사용할 데이터 프레임 생성
        update_stock_info = pd.DataFrame()

        # labeling
        for day in date:

            # 특정일의 Data 추출
            select_day = stock_info.loc[day].copy()
            select_day['label'] = 0
            
            # 특정일의 Row 만큼 반복
            for row in range(len(select_day)):
                
                # 특정일의 현재 row 이후 최대 고가를 추출
                next_price = select_day[-row-1::-1]['고가'].max()

                # 추출한 최대 고가를 label 컬럼에 대입
                select_day.iloc[-row-1,-1] = next_price
                next_price = 0
            
            # 특정일 label이 추가된 DF를 업데이트할 DF에 concat
            update_stock_info = pd.concat([update_stock_info, select_day])
        
        # 업데이트된 DF 저장
        for code in concat_list:
            update_stock_info.to_csv('../data/test_label/label_{0}_{1}.csv'.format(
                search_by_code(code)[0][1:],search_by_code(code)[1]
                ), encoding='utf-8-sig')