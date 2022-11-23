from module.setting import instCpCybos, instStockChart

from datetime import timedelta
from datetime import datetime
from random import uniform
from tqdm import tqdm

import pandas as pd
import time
import os


day_path = '../data/day_data/'
min_path = '../data/min_data/'

day_ord_path = '../data/day_보통주/' 
min_ord_path = '../data/min_보통주/'

day_update_path = '../data/20221121/day_update/'
min_update_path = '../data/20221121/min_update/'

min_fill_path = '../data/20221121/min_fillrow/'

concat_path = '../data/20221121/concat/'

label_path = '../data/20221121/complete/'


# 원하는 폴더에 있는 파일 리스트 추출
def file_open(file_open):
    file_ = os.listdir(f'{file_open}')
    file_.sort()
    
    return file_

#######################################################################################################################################
# 전체 일자 일봉 종목 데이터 가져와서 csv 파일로 저장
def save_day_stock_info_auto(stock_code, end_day, type, day_path=day_path):
    
    day_format = '%Y%m%d'
    minus_day = timedelta(days=5) # 5일치
    
    stock_df = pd.DataFrame()
    
    stock_name = search_by_code(stock_code)

    for day in range(150): # range 범위 수정하지 말 것
        transfer_pre_day = datetime.strptime(end_day, day_format)
        pre_day = datetime.strftime(transfer_pre_day - minus_day, day_format)

        info_second = get_stock_info(stock_code, pre_day, end_day, type) 

        time.sleep(0.15)
        end_day = pre_day
        print(pre_day)

        stock_df = pd.concat([stock_df, info_second], axis=0)
        info_second = pd.DataFrame()
        print(stock_df.shape)
        print(stock_name, 'Count : {0}, 남은 요청 횟수 :{1}'.format(day, instCpCybos.GetLimitRemainCount(1)))
        
        if  instCpCybos.GetLimitRemainCount(1) < 5:
            time.sleep(10)
    
    stock_df.to_csv(f'{day_path}day_{0}_{1}.csv'.format(stock_name[0][1:],stock_name[1]), encoding='utf-8-sig')

    return stock_df


# 전체 일자 분봉 종목 데이터 가져와서 csv 파일로 저장
def save_stock_info_auto(stock_code, end_day, type, min_path=min_path):
    
    day_format = '%Y%m%d'
    minus_day = timedelta(days=1)
    
    stock_df = get_stock_info(stock_code, end_day, end_day, type) # 첫번째 DF 생성
    
    stock_name = search_by_code(stock_code)

    for day in range(740): # range 범위 수정하지 말 것
        transfer_pre_day = datetime.strptime(end_day, day_format) 
        pre_day = datetime.strftime(transfer_pre_day - minus_day, day_format)

        info_second = get_stock_info(stock_code, pre_day, pre_day, type)

        time.sleep(uniform(0.3,0.5))
        end_day = pre_day
        print(pre_day)

        stock_df = pd.concat([stock_df, info_second], axis=0)
        info_second = pd.DataFrame()
        print(stock_df.shape)
        print(stock_name, 'Count : {0}, 남은 요청 횟수 :{1}'.format(day, instCpCybos.GetLimitRemainCount(1)))
        
        if  instCpCybos.GetLimitRemainCount(1) < 5:
            time.sleep(10)
    
    stock_df.to_csv(f'{min_path}{0}_{1}.csv'.format(stock_name[0][1:],stock_name[1]), encoding='utf-8-sig')

    return stock_df

#######################################################################################################################################

# 코스피 코스닥(일봉) 보통주 옮기기 -
def update_day_kospi_kosdaq_list(day_path=day_path, day_ord_path=day_ord_path):
    # 코스피/ 코스닥 리스트 불러오기
    kospi = pd.read_csv('../data/kospi_20221121.csv', encoding='euc-kr')
    kosdaq = pd.read_csv('../data/kosdaq_20221121.csv', encoding='euc-kr')
    # 보통주인 것만 추출
    kospi = kospi[kospi['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]
    kosdaq = kosdaq[kosdaq['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]
    kospi_kosdaq_list = pd.concat([kospi,kosdaq]).to_list()
    
    # 파일 옮기기
    day_list = file_open(day_path)
    for file in day_list:
        for k_k in kospi_kosdaq_list :
            if file.split('_')[-2] == k_k:
                os.replace(day_path  + file, day_ord_path + file)

# 코스피 코스닥(분봉) 보통주 옮기기 -
def update_kospi_kosdaq_list(min_path, min_ord_path):
    # 코스피/ 코스닥 리스트 불러오기
    kospi = pd.read_csv('../data/kospi_20221121.csv', encoding='euc-kr')
    kosdaq = pd.read_csv('../data/kosdaq_20221121.csv', encoding='euc-kr')
    # 보통주인 것만 추출
    kospi = kospi[kospi['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]
    kosdaq = kosdaq[kosdaq['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]
    kospi_kosdaq_list = pd.concat([kospi,kosdaq]).to_list()
    # 파일 옮기기
    min_list = file_open(min_path)
    for file in min_list:
        for k_k in kospi_kosdaq_list :
            if file.split('_')[-2] == k_k:
                os.replace(min_path + file, min_ord_path + file)
                
                
#######################################################################################################################################


# 코스피 코스닥(일봉) 업데이트
def update_day_stock_info(day_ord_path=day_ord_path, day_update_path=day_update_path):
    day_ord_list = file_open(day_ord_path)
    for file_name in tqdm(day_ord_list):
        temp_df = pd.read_csv(f'{day_ord_path}{file_name}', index_col='Unnamed: 0', encoding='utf-8 sig')
        
        stock_code = file_name.split('_')[-2] # 종목 코드 분할
        
        start_day = str(temp_df.index[0])

      

        instStockChart.SetInputValue(0, 'A'+stock_code) # 종목명
        instStockChart.SetInputValue(1, ord('1')) # 1 : 기간으로 요청, 2: 개수로 요청
        instStockChart.SetInputValue(3, start_day) # 요청 시작일
        instStockChart.SetInputValue(2, today) # 요청 종료일
        instStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17,18, 19,20,21,22,23,24,25,26])
        instStockChart.SetInputValue(6, ord('D')) # 'D' : 일봉, 'm' : 분봉
        instStockChart.SetInputValue(9, ord('1'))

        instStockChart.BlockRequest() # 위 정보로 요청

        numrow, numcolumn = instStockChart.GetHeaderValue(3), instStockChart.GetHeaderValue(2)

        index = []
        for i in range(numrow):
            index_ = str(instStockChart.GetDataValue(0,i))
            index.append(index_)

        stock_info = pd.DataFrame(columns=numcolumn[1:], index=index)

        for num in range(numrow):
            for col in range(len(numcolumn)):
                # 1,2,3,4,5,6,7,8,9, 10
                stock_info.iloc[num, col-1] = str(instStockChart.GetDataValue(col,num))

        update_day_df = pd.concat([stock_info, temp_df])
        
        update_day_df.to_csv(f'{day_update_path}{file_name}', encoding='utf-8 sig')

    return update_day_df



# 코스피 코스닥(분봉) 업데이트
def update_min_stock_info(min_ord_path=min_ord_path, min_update_path=min_update_path):
    min_ord_list = file_open(min_ord_path)
    for file_name in min_ord_list:
        stock_code = file_name.split('_')[-2]
        temp_df = pd.read_csv(f'{min_ord_path}{file_name}', index_col='Unnamed: 0', encoding='utf-8 sig')
        
        last_day = str(temp_df.index[0]) # 20221031

        day_format = '%Y%m%d'
        plus_day = timedelta(days=1)

        transfer_last_day = datetime.strptime(last_day, day_format) # 20221031
        start_day = datetime.strftime(transfer_last_day + plus_day, day_format) # 20221101

        today = str(datetime.today().year) + str(datetime.today().month) + str(datetime.today().day) # 20221116

        

        while True:

            instStockChart.SetInputValue(0, 'A'+stock_code) # 종목명
            instStockChart.SetInputValue(1, ord('1')) # 1 : 기간으로 요청, 2: 개수로 요청
            instStockChart.SetInputValue(3, start_day) # 요청 시작일
            instStockChart.SetInputValue(2, start_day) # 요청 종료일
            instStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17,18, 19,20,21,22,23,24,25,26])
            instStockChart.SetInputValue(6, ord('m')) # 'D' : 일봉, 'm' : 분봉
            instStockChart.SetInputValue(9, ord('1'))

            instStockChart.BlockRequest() # 위 정보로 요청

            numrow, numcolumn = instStockChart.GetHeaderValue(3), instStockChart.GetHeaderValue(2)

            index = []
            for i in range(numrow):
                index_ = str(instStockChart.GetDataValue(0,i))
                index.append(index_)

            stock_info = pd.DataFrame(columns=numcolumn[1:], index=index)

            for num in range(numrow):
                for col in range(len(numcolumn)):
                    # 1,2,3,4,5,6,7,8,9, 10
                    stock_info.iloc[num, col-1] = str(instStockChart.GetDataValue(col,num))

            update_min_df = pd.concat([stock_info, temp_df])
            
            
            start_day = datetime.strftime(datetime.strptime(start_day, day_format) + timedelta(days=1), day_format)
            transfer_end_day = datetime.strftime(datetime.strptime(today, day_format), day_format) # 20221116
            time.sleep(uniform(0.15, 0.3))

            if instCpCybos.GetLimitRemainCount(1) < 3:
                time.sleep(10)

            if start_day == transfer_end_day:
                update_min_df.to_csv(f'{min_update_path}{file_name}', encoding='utf-8 sig')
                break

    return update_min_df


######################################################################################################################################

# 분봉의 빈 로우 채우기
def update_fillrow(min_update_path=min_update_path, min_fill_path=min_fill_path):
    
    template = pd.read_csv(f'{min_update_path}005930_삼성전자.csv', encoding='utf-8 sig')
    template = template.set_index(['Unnamed: 0', '시간'])
    template = template.notnull().replace(True, np.NaN)
    template.to_csv('../data/fillrow_template.csv', encoding='utf-8 sig')

    min_update_list = file_open(min_update_path)
    for file_name in min_update_list:
        stock_info = pd.read_csv(f'{min_update_path}{file_name}', encoding='utf-8 sig')
        stock_info = stock_info.set_index(['Unnamed: 0', '시간'])

        stock_info = pd.merge(template, stock_info, how='left', left_index=True, right_index=True)

        stock_info = stock_info.drop(columns=stock_info.columns[0:23], axis=1)

        columns_temp = stock_info.columns

        bin_columns = []
        for column in columns_temp:
            bin_columns.append(column.split('_')[0])

        stock_info.columns = bin_columns

        stock_info = stock_info.reset_index()
        stock_info = stock_info.rename(columns={'Unnamed: 0' : '날짜'})

        stock_info[['거래량','거래대금']] = stock_info[['거래량','거래대금']].fillna(0)
        stock_info = stock_info.bfill()

        stock_info.to_csv(f'{min_fill_path}{file_name}', encoding='utf-8 sig')
        
           

######################################################################################################################################



# 분봉 일봉 합치기
def save_min_day_concat_info(min_fill_path = min_fill_path,day_update_path=day_update_path, concat_path= concat_path):
    min_fill_list = file_open(min_fill_path)
    day_update_list = file_open(day_update_path)
    for min_df, day_df in zip(min_fill_list, day_update_list):
        stock_min_df = pd.read_csv(f'{min_fill_path}{min_df}', encoding='utf-8 sig')
        stock_day_df = pd.read_csv(f'{day_update_path}{day_df}', encoding='utf-8 sig')
        
        input_list = ['전일대비','상장주식수','시가총액','외국인주문한도수량'
                    ,'외국인주문가능수량','외국인현보유수량','외국인현보유비율'
                    ,'수정주가일자','수정주가비율','기관순매수량','기관누적순매수량'
                    ,'등락주선','등락비율','예탁금','주식회전율','거래성립률']                                  
        list_ = ['시간','시가','고가','저가','종가','거래량','거래대금','누적체결매도수량', '누적체결매수수량'
                 ,'등락주선','등락비율','예탁금','주식회전율','거래성립률']
            
        stock_min_df = stock_min_df.drop(input_list, axis=1)
        stock_day_df = stock_day_df.drop(list_, axis=1)
        
        
        concat_df = pd.merge(stock_min_df, stock_day_df,on='Unnamed: 0', how='left')
        concat_df = concat_df.rename(columns={'Unnamed: 0':'날짜'})
        
        concat_df.to_csv(f'{concat_path}concat_{min_df}', encoding='utf-8 sig', index=False)          
        
    return concat_df

######################################################################################################################################

# Concat 완료된 데이터 Labeling 추가
def save_label_stock_info(concat_path=concat_path, label_path=label_path):
    concat_list = file_open(concat_path)
    for file_name in concat_list:
        stock_info = pd.read_csv(f'{concat_path}{file_name}', index_col=0)
        
        code_list =  []
        code_list.append(file_name.split('_')[-2])
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
        for code in code_list:
            update_stock_info.to_csv(f'{label_path}{code}.csv', encoding='utf-8-sig')


######################################################################################################################################
