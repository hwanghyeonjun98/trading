from datetime import date
import pandas as pd
import os
import time
import glob
import shutil

from final_dbconnect import DBConnection
from pandas.tseries.offsets import BDay
from module.selenium_crawling import selenium_driver_load, By

# 날짜 지정 필수
today = str(date.today()).replace('-','')
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]
print('실시간 트레이딩 기준 날짜 : ' + today)

def get_pymysql_db_list(conn, db_name):

    # 현재 DB 내 존재하는 테이블(종목) 추출
    sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{0}'".format(db_name)

    result = conn.execute(sql)
    db_list = [item[0] for item in result.fetchall()]

    return db_list


def get_investing_data(conn, investing_data_list):

    investing_df = pd.DataFrame()

    # 현재 DB 내 존재하는 테이블(종목) 추출
    for table in investing_data_list:
        conn = DBConnection().get_sqlalchemy_connect_ip()
        sql = "SELECT * FROM investing_data.`{0}` ORDER BY 날짜 DESC LIMIT 1 ".format(table)

        result = conn.execute(sql)

        temp_df = pd.DataFrame(result.fetchall())
        investing_df = pd.concat([investing_df, temp_df], axis=1)
    
    investing_df.drop(columns='날짜', axis=1, inplace=True) # 어제 날짜
    investing_df.rename(index={0:today}, inplace=True) # 오늘 날짜로 reindex
    
    return investing_df


def get_krx_target(path):

    target = "./download/target/target*.csv"
    csv_list = glob.glob(target)
    print(csv_list)

    if len(csv_list) >= 1: # 파일이 있는 경우
        
        csv_date = csv_list[0].split('.')[0][-8:] # 날짜 확인
        
        if csv_date != today: # 날짜가 다른 경우
            os.remove(csv_list[0])

        else:
            return

    driver = selenium_driver_load(
        './driver/chromedriver'
        , "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201"
        , path
    )
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

    target_path = "./download/target/data*.csv"
    new_csv_list = glob.glob(target_path)

    shutil.move(new_csv_list[0], f'./download/target/target_{today}.csv')

def get_target_stock_list():

    # 대상 종목 추출
    target_df = pd.read_csv(f'./download/target/target_{today}.csv', encoding='euc-kr')
    target_df = target_df[['종목코드','시장구분','등락률','거래대금','시가총액']]
    target_df['value_cap_ratio'] = target_df['거래대금'] / target_df['시가총액']

    gubun, market_cap, ratio = target_df['시장구분'], target_df['시가총액'], target_df['등락률']
    kospi = target_df[(gubun == 'KOSPI') & (market_cap> 300000000000) & (ratio > 0)].sort_values(by='value_cap_ratio', ascending=False).iloc[0:10]
    kosdaq = target_df[(gubun == 'KOSDAQ') & (market_cap> 100000000000) & (market_cap < 500000000000) & (ratio > 0)].sort_values(by='value_cap_ratio', ascending=False).iloc[0:10]

    kospi_list = kospi['종목코드'].to_list()
    kosdaq_list = kosdaq['종목코드'].to_list()

    return kospi_list, kosdaq_list





def get_target(path):
    # 대상 종목 설정
    get_krx_target(path=path)
    kospi_list, kosdaq_list = get_target_stock_list()
    
    # Investing Data 생성
    
    investing_data_list = get_pymysql_db_list(DBConnection().get_sqlalchemy_connect_ip(), 'investing_data')
    investing_df = get_investing_data(DBConnection().get_sqlalchemy_connect_ip(), investing_data_list)

    return kospi_list, kosdaq_list, investing_df
