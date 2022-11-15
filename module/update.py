from module.setting import instCpCodeMgr, instStockChart
from datetime import datetime
import pandas as pd
import re
import os
from tqdm import tqdm


# 코드명이 A로 시작하는 것만 추출
def update_stock_list():
        stock_list = []
        stock_list = stock_list + list(instCpCodeMgr.GetStockListByMarket(2))
        stock_list_real = []
        p = re.compile('^A')

        for stock in stock_list:
                if p.match(str(stock)) != None:
                        stock_list_real.append(stock)
        return stock_list_real
                    


# 코스피 코스닥(분봉) 보통주 옮기기 -
def update_kospi_kosdaq_list(folder_org, folder_re):
    kospi = pd.read_csv('../data/kospi_20221110.csv', encoding='euc-kr')
    kosdaq = pd.read_csv('../data/kosdaq_20221110.csv', encoding='euc-kr')

    kospi = kospi[kospi['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]
    kosdaq = kosdaq[kosdaq['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]

    
    kospi_kosdaq_list = pd.concat([kospi,kosdaq]).to_list()

    file_source = f'../data/{folder_org}/'
    file_destination = f'../data/{folder_re}/'
    
    files_list = os.listdir(file_source)
    
    for file in tqdm(files_list):
        for k_k in kospi_kosdaq_list :
            if file.split('_')[-2] == k_k:
                os.replace(file_source + file, file_destination + file)


# 코스피 코스닥(일봉) 보통주 옮기기 -
def update_day_kospi_kosdaq_list(folder_org, folder_re):
    kospi = pd.read_csv('../data/kospi_20221110.csv', encoding='euc-kr')
    kosdaq = pd.read_csv('../data/kosdaq_20221110.csv', encoding='euc-kr')

    kospi = kospi[kospi['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]
    kosdaq = kosdaq[kosdaq['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]

    
    kospi_kosdaq_list = pd.concat([kospi,kosdaq]).to_list()

    file_source = f'../data/{folder_org}/'
    file_destination = f'../data/{folder_re}/'
    
    files_list = os.listdir(file_source)
    
    for file in tqdm(files_list):
        for k_k in kospi_kosdaq_list :
            if file.split('_')[-2] == k_k:
                os.replace(file_source + file, file_destination + file)

# 코스피 코스닥(일봉) 업데이트
def update_day_stock_info(file_name):
    
    stock_code = file_name.split('_')[-2]
    temp_df = pd.read_csv(f'../data/test1/{file_name}', index_col='Unnamed: 0', encoding='utf-8 sig')
    start_day = str(temp_df.index[0])

    today = str(datetime.today().year) + str(datetime.today().month) + str(datetime.today().day)

    print(stock_code, start_day, today)

    instStockChart.SetInputValue(0, 'A'+stock_code) # 종목명
    instStockChart.SetInputValue(1, ord('1')) # 1 : 기간으로 요청, 2: 개수로 요청
    instStockChart.SetInputValue(3, start_day) # 요청 시작일
    instStockChart.SetInputValue(2, today) # 요청 종료일
    instStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17,18, 19,20,21,22,23,24,25,26])
    instStockChart.SetInputValue(6, ord('D')) # 'D' : 일봉, 'm' : 분봉
    instStockChart.SetInputValue(9, ord('1'))

    instStockChart.BlockRequest() # 위 정보로 요청

    numrow, numcolumn = instStockChart.GetHeaderValue(3), instStockChart.GetHeaderValue(2)

    print(numrow, numcolumn)

    index = []
    for i in range(numrow):
        index_ = str(instStockChart.GetDataValue(0,i))
        index.append(index_)

    stock_info = pd.DataFrame(columns=numcolumn[1:], index=index)

    for num in range(numrow):
        for col in range(len(numcolumn)):
            # 1,2,3,4,5,6,7,8,9, 10
            stock_info.iloc[num, col-1] = str(instStockChart.GetDataValue(col,num))

    temp_df = pd.concat([stock_info, temp_df])
    
    temp_df.to_csv(f'../data/temp/{file_name}', encoding='utf-8 sig')

    return temp_df

# 코스피 코스닥(분봉) 업데이트