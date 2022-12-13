import os
import csv
import glob
import time
import shutil
import pymysql
import numpy as np
import pandas as pd


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from sqlalchemy import create_engine
from datetime import datetime
from datetime import timedelta, date
from tqdm import tqdm
from random import uniform
from final_dbconnect import DBConnection
from module.setting import instCpCodeMgr, instStockChart, instCpCybos

today = str(date.today()).replace('-','')


# mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
def sqlalchemy_connect_ip(ip_address, db_name):
    engine = create_engine("mysql+pymysql://admin:"
                +"big15" # user password
                +"@{0}:3306/{1}?charset=utf8".format(ip_address, db_name)
                , encoding='utf8')
    
    return engine.connect()


def get_pymysql_connection(ip_address, db_name):

    conn = pymysql.connect(host=ip_address, user='admin', password='big15'
                        , db=db_name, charset='utf8')

    return conn
    
def get_pymysql_stock_list(conn, db_name):
    # 현재 DB 내 존재하는 테이블(종목) 추출
    sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '{0}'".format(db_name)

    with conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            result = [item[0] for item in cur.fetchall()]
            cur.close()

            return result

def get_krx_stock_list(user):

    target = r"\\DESKTOP-H2H6JNB\data\kos*.csv"
    csv_list = glob.glob(target)

    if len(csv_list) >= 1:
        
        csv_date = csv_list[0].split('.')[0][-8:]
        
        if csv_date != today:

            os.remove(csv_list[0])
            os.remove(csv_list[1])
        else:
            return
        
    driver = webdriver.Chrome("./chromedriver")

    driver.get("http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201")
    driver.implicitly_wait(20)
    time.sleep(4)
    driver.find_element(By.XPATH, '//*[@id="MDCSTAT019_FORM"]/div[1]/div/table/tbody/tr/td/label[2]').click()
    time.sleep(1.5)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="MDCSTAT019_FORM"]/div[2]/div[1]/p[2]/button[2]').click()	
    time.sleep(1.5)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="ui-id-1"]/div/div[2]').click()
    time.sleep(1.5)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="MDCSTAT019_FORM"]/div[1]/div/table/tbody/tr/td/label[3]').click()
    time.sleep(1.5)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="MDCSTAT019_FORM"]/div[2]/div[1]/p[2]/button[2]').click()	
    time.sleep(1.5)
    driver.implicitly_wait(20)
    driver.find_element(By.XPATH, '//*[@id="ui-id-3"]/div/div[2]').click()
    time.sleep(1.5)
    driver.close()

    target = r"C:\Users\{0}\Downloads\data*.csv".format(user)

    new_csv_list = glob.glob(target)

    file_size_1 = os.path.getsize(new_csv_list[0])
    file_size_2 = os.path.getsize(new_csv_list[1])

    if file_size_1 < file_size_2:
        shutil.move(new_csv_list[0], fr"\\DESKTOP-H2H6JNB\data\kospi_{today}.csv")
        shutil.move(new_csv_list[1], fr"\\DESKTOP-H2H6JNB\data\kosdaq_{today}.csv")
    else:
        shutil.move(new_csv_list[1], fr"\\DESKTOP-H2H6JNB\data\kospi_{today}.csv")
        shutil.move(new_csv_list[0], fr"\\DESKTOP-H2H6JNB\data\kosdaq_{today}.csv")

def get_compare_list(stock_list):
# stock code가 테이블이 존재하는 비교

    kospi = pd.read_csv(fr'\\DESKTOP-H2H6JNB\data\kospi_{today}.csv', encoding='euc-kr')
    kosdaq = pd.read_csv(fr'\\DESKTOP-H2H6JNB\data\kosdaq_{today}.csv', encoding='euc-kr')

    kospi = kospi[kospi['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]
    kosdaq = kosdaq[kosdaq['주식종류'] == '보통주'].iloc[:,[1,-3]].iloc[:,0]

    kospi_kosdaq_list = pd.concat([kospi,kosdaq]).to_list()

    exist_list = []
    empty_list = []

    for code in kospi_kosdaq_list:
        if code in stock_list:
            exist_list.append(code)
        elif code not in stock_list:
            empty_list.append(code)
    
    exist_list.sort()
    empty_list.sort()
    
    return exist_list, empty_list

def update_pymysql_exist(code, type, conn):
# 존재할 경우, 대신증권에서 해당 종목 일봉 분봉 업데이트문

    sql = "SELECT MAX(날짜) FROM STOCK_INFO.{0} ".format(code)

    cur = conn.cursor()
    cur.execute(sql)
    max_day = cur.fetchone()[0] # 마지막 업데이트 날짜

    day_format = '%Y%m%d'
    start_day = datetime.strftime(datetime.strptime(str(max_day), day_format) + timedelta(days=1), day_format)

    # 최종 업데이트 날짜가 오늘 날짜와 같은 경우 배제
    if (str(max_day) != today):
        temp_df = pd.DataFrame()
        while True:
            instStockChart.SetInputValue(0, 'A'+code) # 종목명
            instStockChart.SetInputValue(1, ord('1')) # 1 : 기간으로 요청, 2: 개수로 요청
            instStockChart.SetInputValue(3, start_day) # 요청 시작일
            instStockChart.SetInputValue(2, start_day) # 요청 종료일
            instStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19,20,21,22,23,24,25,26])
            instStockChart.SetInputValue(6, ord(type)) # 'D' : 일봉, 'm' : 분봉
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
                
            stock_info = stock_info.apply(pd.to_numeric)
            temp_df = pd.concat([stock_info, temp_df])

            start_day = datetime.strftime(datetime.strptime(start_day, day_format) + timedelta(days=1), day_format)
            transfer_end_day = datetime.strftime(datetime.strptime(today, day_format), day_format)
            time.sleep(uniform(0.15, 0.3))

            if instCpCybos.GetLimitRemainCount(1) < 3:
                time.sleep(10)

            if start_day > transfer_end_day:
                temp_df = temp_df.reset_index().rename(columns={'index':'날짜'})
                
                return temp_df
    else:
        return pd.DataFrame()

def update_pymysql_empty(code, type, conn, today):
# 존재할 경우, 대신증권에서 해당 종목 일봉 분봉 업데이트문
    
    day_format = '%Y%m%d'
    minus_day = timedelta(days=1)

    temp_df = pd.DataFrame()

    for day in range(730):
        instStockChart.SetInputValue(0, 'A'+code) # 종목명
        instStockChart.SetInputValue(1, ord('1')) # 1 : 기간으로 요청, 2: 개수로 요청
        instStockChart.SetInputValue(3, today) # 요청 시작일
        instStockChart.SetInputValue(2, today) # 요청 종료일
        instStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19,20,21,22,23,24,25,26])
        instStockChart.SetInputValue(6, ord(type)) # 'D' : 일봉, 'm' : 분봉
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
        temp_df = pd.concat([stock_info, temp_df])

        today = datetime.strftime(datetime.strptime(today, day_format) - timedelta(days=1), day_format)
        transfer_end_day = datetime.strftime(datetime.strptime(today, day_format), day_format)
        time.sleep(uniform(0.15, 0.3))

        if instCpCybos.GetLimitRemainCount(1) < 3:
            time.sleep(10)
            
        temp_df = temp_df.reset_index().rename(columns={'index':'날짜'})
        return temp_df

# 삼성전자 종목 업데이트 우선 수행 후 template 생성

def save_samsung_template(conn):
    day_format = '%Y%m%d'

    yesterday = datetime.strftime(datetime.strptime(today, day_format) - timedelta(days=1), day_format)
    template = update_pymysql_exist('005930', 'm', conn)
    template = template.reset_index()
    template = template.set_index(['날짜', '시간'])
    template = template.notnull().replace(True, np.NaN)
    y_template = pd.read_csv(r'\\DESKTOP-H2H6JNB\data\{0}_fillrow_template.csv'.format(yesterday), encoding='utf-8 sig')
    y_template = y_template.rename(columns={'Unnamed: 0' : '날짜'})
    y_template = y_template.set_index(['날짜', '시간'])
    template = pd.concat([template, y_template], axis=0, ignore_index=False)
    template.to_csv(r'\\DESKTOP-H2H6JNB\data\{0}_fillrow_template.csv'.format(today), encoding='utf-8 sig')
    template = template.drop(['index'], axis=1)
    template.reset_index(inplace=True)
    template = template.loc[:,['날짜', '시간']]

    return template


# 종목별 업데이트, fillrow, concat 수행
def update_fillrow(min_df, template):
    
    min_df = pd.merge(template, min_df, on=['날짜', '시간'], how='left')
    min_df = min_df.sort_index()

    min_df[['거래량','거래대금']] = min_df[['거래량','거래대금']].fillna(0)
    min_df = min_df.bfill()
    min_df = min_df.dropna()

    return min_df


# 분봉 일봉 concate 진행
def update_concat(min_df, day_df):

    min_drop_list = ['전일대비','상장주식수','시가총액','외국인주문한도수량'
                ,'외국인주문가능수량','외국인현보유수량','외국인현보유비율'
                ,'수정주가일자','수정주가비율','기관순매수량','기관누적순매수량'
                ,'등락주선','등락비율','예탁금','주식회전율','거래성립률']                                  
    day_drop_list = ['시간','시가','고가','저가','종가','거래량','거래대금','누적체결매도수량', '누적체결매수수량'
                ,'등락주선','등락비율','예탁금','주식회전율','거래성립률']
        
    stock_min_df = min_df.drop(min_drop_list, axis=1)
    stock_day_df = day_df.drop(day_drop_list, axis=1)
    
    concat_df = pd.merge(stock_min_df, stock_day_df, on='날짜', how='left')
    concat_df.dropna(inplace=True)

    return concat_df


# label 추가
def update_label(concat_df):

    # 데이터 프레임에서 날짜 인덱스 추출
    concat_df.set_index('날짜', inplace=True)
    date = concat_df.index.unique()
    # label 컬럼 추가 후 0으로 초기화
    concat_df['label'] = 0
    # 업데이트에 사용할 데이터 프레임 생성
    update_stock_info = pd.DataFrame()
    # labeling
    for day in date:
        # 특정일의 Data 추출
        select_day = concat_df.loc[day].copy()
        select_day['label'] = 0
        # 특정일의 Row 만큼 반복
        for row in range(len(select_day)):
            # 특정일의 현재 row 이후 최대 고가를 추출
            next_price = select_day[-row-1::-1]['고가'].max()
            # 추출한 최대 고가를 label 컬럼에 대입
            select_day.iloc[-row-1,-1] = next_price
            # next_price = 0
        # 특정일 label이 추가된 DF를 업데이트할 DF에 concat
        update_stock_info = pd.concat([update_stock_info, select_day])

    trans = update_stock_info.loc[:,['고가','label']]
    trans['고가'] = trans['고가'].astype('float')
    trans['label'] = trans['label'].astype('float')
    trans = trans.rename(columns={'label':'pct_label'}).T

    get_trans = trans.pct_change().T.iloc[:,-1]
    update_stock_info = pd.concat([update_stock_info, get_trans], axis=1)
    update_stock_info = update_stock_info.drop(['label'], axis=1)

    update_stock_info['pct_label'] = update_stock_info['pct_label'].mul(100)
    update_stock_info['pct_label'] = update_stock_info['pct_label'].round(1)
    update_stock_info.reset_index(inplace=True)

    return update_stock_info


# Data csv => SQL에 추가
def sqlalchemy_update_insert(update_df, code, type, conn):

    update_df['년'] = update_df['날짜'].apply(str).str[:4]
    update_df['월'] = update_df['날짜'].apply(str).str[4:6]
    update_df['일'] = update_df['날짜'].apply(str).str[6:8]
    update_df.sort_index(ascending=False, inplace=True)
    # name= table명
    # con= connect할 때 들어가는 아이디 비밀번호 등등
    # if_exists= 'append' : 기존 테이블이 있는 경우 데이터를 추가
    # 'fail' : 기존 테이블이 있는 경우 아무일도 없지만 없을 경우 valuesError뜸
    # 'replace' : 기존 테이블이 있을 경우, 기존 테이블을 삭제하고 다시 테이블을
    count = update_df.to_sql(name='{0}'.format(code), con=conn, if_exists=type, index=False)
    
    
    
def db_list_update(computer_name):

    pct_error_list = []
    
    pymysql_conn =DBConnection().get_pymysql_connection()
    sqlalchemy_conn = DBConnection().get_sqlalchemy_connect_ip()

    stock_list = get_pymysql_stock_list(pymysql_conn, 'stock_info')
    print(stock_list)
    get_krx_stock_list(user=computer_name)
    exist_list, empty_list = get_compare_list(stock_list)
    
    template = save_samsung_template(pymysql_conn)

    for code in exist_list:
        
        print('현재 업데이트 중인 종목명 : ' + code)
        min_df = update_pymysql_exist(code, 'm', pymysql_conn)
        if min_df.empty == False:
            day_df = update_pymysql_exist(code, 'D', pymysql_conn)
            min_df = update_fillrow(min_df, template)
            concat_df = update_concat(min_df, day_df)
            update_df = update_label(concat_df)
            if len(update_df[update_df['pct_label'] < 0]):
                pct_error_list.append(code)
                print('pct_label 에러 발생' + code)

            sqlalchemy_update_insert(update_df, code, 'append', sqlalchemy_conn)
    if len(pct_error_list) > 0:
        for stock in pct_error_list:
            print('에러 발생 종목 리스트 : ' + stock)
    else:
        print('업데이트가 완료되었습니다.')
        
    if len(empty_list) > 0 :
    
        error_list = []
        
        for code in empty_list:
            print('현재 업데이트 중인 종목명 : ' + code)
            try:
                min_df = update_pymysql_empty(code, 'm', pymysql_conn, today)
                day_df = update_pymysql_empty(code, 'D', pymysql_conn, today)

                min_df = update_fillrow(min_df, template)
                concat_df = update_concat(min_df, day_df)
                update_df = update_label(concat_df)
                sqlalchemy_update_insert(update_df, code, 'replace', sqlalchemy_conn)
            except:
                print('에러 발생 종목 : ' + code)
                error_list.append(code)
        
        if len(error_list) > 0:
            for stock in error_list:
                print('에러 발생 종목 리스트 : ' + stock)
        else:
            print('업데이트가 완료되었습니다.')
        
    conn.close()
    
    