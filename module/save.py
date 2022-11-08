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
    
    stock_df.to_csv(r'\\DESKTOP-H2H6JNB\data\{0}_{1}.csv'.format(stock_name[0][1:],stock_name[1]), encoding='utf-8-sig')

    return stock_df


# 리스트 수정본 저장
def save_stock_list_real(n, code, end_day, type):
    for code in stock_list_real[n:]:
        save_stock_info_auto(code, end_day, type)
        

# 분봉 일봉 합쳐서 저장
def save_min_day_concat():
    # 파일 불러오기
    files_m = os.listdir('../data')
    files_d = os.listdir('../data_day') 
    
    # 파일 정렬하기
    files_m.sort()
    files_d.sort()
    
    for j, (min_df, day_df) in enumerate(zip(files_m, files_d)):
        globals()[f'data_m{j}'] = pd.read_csv(f'../data/{min_df}', index_col='Unnamed: 0')
        globals()[f'data_d{j}'] = pd.read_csv(f'../data_day/{day_df}', index_col='Unnamed: 0')
        
        concat_list = []
        concat_list.append('A' + files_m[j].split('_')[-2])
        
        for v in tqdm(globals()[f'data_m{j}'].index):
            input_list = ['전일대비','상장주식수','시가총액','외국인주문한도수량'
                    ,'외국인주문가능수량','외국인현보유수량','외국인현보유비율'
                    ,'수정주가일자','수정주가비율','기관순매수량','기관누적순매수량']
            
            globals()[f'data_m{j}'].loc[v, input_list] = globals()[f'data_d{j}'].loc[v, input_list].values
        for code in concat_list:        
            globals()[f'data_m{j}'].to_csv('../data_concat/concat_{0}_{1}.csv'.format(
                            search_by_code(code)[0][1:],search_by_code(code)[1]
                            ), encoding='utf-8-sig') 