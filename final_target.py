from module.setting import instCpStockCode, instCpCodeMgr, instStockChart, instCpCybos, instCpTdUtil, instCpTd0311, instCpTd6033
from module import connection, get, save, search, update
from sqlalchemy import create_engine
from datetime import timedelta, date
from datetime import datetime
import pandas as pd
import pymysql
import pandas as pd
import os
import time

from final_dbconnect import DBConnection
from final_db_update import *

# 날짜 지정 필수
today = str(date.today()).replace('-','')
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]
print('실시간 트레이딩 기준 날짜 : ' + today)

def get_krx_target():

    target_path = r"\\DESKTOP-H2H6JNB\data\target*.csv"
    csv_list = glob.glob(target_path)

    if len(csv_list) >= 1: # 파일이 있는 경우
        
        csv_date = csv_list[0].split('.')[0][-8:] # 날짜 확인
        
        if csv_date != today: # 날짜가 다른 경우
            os.remove(csv_list[0])

        else:
            return

    driver = webdriver.Chrome("./chromedriver")

    driver.get("http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201")
    driver.implicitly_wait(20)
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="jsMdiMenu"]/div[4]/ul/li[1]/ul/li[2]/div/div[1]/ul/li[2]/ul/li[1]/a').click()
    time.sleep(1.5)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="jsMdiMenu"]/div[4]/ul/li[1]/ul/li[2]/div/div[1]/ul/li[2]/ul/li[1]/ul/li[1]/a').click()
    time.sleep(20)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="MDCSTAT015_FORM"]/div[2]/div/p[2]/button[2]/img').click()
    time.sleep(1.5)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="ui-id-1"]/div/div[2]/a').click()	
    time.sleep(1.5)
    driver.implicitly_wait(20)
    driver.close()

    target_path = r"C:Users/TJ/Downloads/data*.csv"
    new_csv_list = glob.glob(target_path)

    shutil.move(new_csv_list[0], fr"\\DESKTOP-H2H6JNB\data\target_{today}.csv")

def get_target_stock_list():

    # 대상 종목 추출
    target_df = pd.read_csv(fr'\\DESKTOP-H2H6JNB\data\target_{today}.csv', encoding='euc-kr')
    target_df = target_df[['종목코드','시장구분','등락률','거래대금','시가총액']]
    target_df['value_cap_ratio'] = target_df['거래대금'] / target_df['시가총액']

    gubun, market_cap, ratio = target_df['시장구분'], target_df['시가총액'], target_df['등락률']
    kospi = target_df[(gubun == 'KOSPI') & (market_cap> 300000000000) & (ratio > 0)].sort_values(by='value_cap_ratio', ascending=False).iloc[0:10]
    kosdaq = target_df[(gubun == 'KOSDAQ') & (market_cap> 100000000000) & (market_cap < 500000000000) & (ratio > 0)].sort_values(by='value_cap_ratio', ascending=False).iloc[0:10]

    kospi_list = kospi['종목코드'].to_list()
    kosdaq_list = kosdaq['종목코드'].to_list()

    return kospi_list, kosdaq_list





def get_target():
    # 대상 종목 설정
    get_krx_target()
    kospi_list, kosdaq_list = get_target_stock_list()
    
    # Investing Data 생성
    sqlalchemy_conn = DBConnection().get_sqlalchemy_connect_ip()
    investing_data_list = get_pymysql_db_list(sqlalchemy_conn, 'investing_data')
    investing_df = get_investing_data(sqlalchemy_conn, investing_data_list)

    return kospi_list, kosdaq_list, investing_df
