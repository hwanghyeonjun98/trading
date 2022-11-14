from module.setting import instCpCodeMgr

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