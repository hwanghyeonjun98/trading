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


stock_list = ['A000020', 'A000040', 'A000050', 'A000060', 'A000070', 'A000100', 'A000120', 'A000140', 'A000150', 'A000180']

# 날짜 지정 필수
today = str(date.today() - timedelta(days=1)).replace('-','')
yesterday = str(date.today() - timedelta(days=2)).replace('-','')

# mysql connect하기 위한 아이디 비밀번호 포트 데이터베이스 등록 및 conn 리턴
def sqlalchemy_connect_ip(ip_address, db_name):
    engine = create_engine("mysql+pymysql://admin:"
                +"big15" # user password
                +"@{0}:3306/{1}?charset=utf8".format(ip_address, db_name)
                , encoding='utf8')
    
    return engine.connect()

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
        conn = sqlalchemy_connect_ip('192.168.50.123', 'investing_data')
        sql = "SELECT * FROM investing_data.`{0}` ORDER BY 날짜 DESC LIMIT 1 ".format(table)

        result = conn.execute(sql)

        temp_df = pd.DataFrame(result.fetchall())
        investing_df = pd.concat([investing_df, temp_df], axis=1)
    
    investing_df.drop(columns='날짜', axis=1, inplace=True) # 어제 날짜
    investing_df.rename(index={0:today}, inplace=True) # 오늘 날짜로 reindex
    
    return investing_df

def get_pymysql_day_stock(conn, code, yesterday, investing_df):

    code = code[-6:]
    sql = "SELECT 날짜, 전일대비, 상장주식수, 시가총액, 외국인현보유수량, 외국인현보유비율, 기관순매수량, 기관누적순매수량, 년, 월, 일 FROM stock_info.`{0}` WHERE 날짜={1} ORDER BY 시간 DESC LIMIT 1".format(code, yesterday)

    result = conn.execute(sql)

    target_df = pd.DataFrame(result.fetchall())
    target_df.set_index('날짜', inplace=True)
    target_df.rename(index={int(yesterday):today}, inplace=True)
    target_df = pd.concat([target_df, investing_df], axis=1)

    return target_df

def get_realtime_stock_info(code, today):
    
    instStockChart.SetInputValue(0, code) # 종목명
    instStockChart.SetInputValue(1, ord('2')) # 1 : 기간으로 요청, 2: 개수로 요청
    instStockChart.SetInputValue(3, today) # 요청 시작일
    instStockChart.SetInputValue(2, today) # 요청 종료일
    instStockChart.SetInputValue(4, 1) # 요청 개수
    '''
    # 요청할 데이터 종류(리스트 형태로 요청 가능)
    0 : 날짜, 1 : 시간 - hhmm, 2 : 시가, 3 : 고가, 4 : 저가, 5 : 종가
    6 : 전일대비, 7 : 없음, 8 : 거래량, 9 : 거래대금, 10 : 누적체결매도수량
    11 : 누적체결매수수량, 12 : 상장주식수, 13 : 시가총액, 14 : 외국인주문한도수량, 15 : 외국인주문가능수량
    16 : 외국인현보유수량, 17 : 외국인현보유비율, 18 : 수정주가일자, 19 : 수정주가비율, 20 : 기관순매수
    21 : 기관누적순매수, 22 : 등락주선, 23 : 등락비율, 24 : 예탁금, 25 : 주식회전율
    26 : 거래성립률
    '''
    instStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 8, 9, 10, 11])
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

    if instCpCybos.GetLimitRemainCount(1) < 3:
        while True:
            if instCpCybos.GetLimitRemainCount(1) > 3:
                break
            time.sleep(0.1)

    return stock_info.iloc[0:1]

# buysell => str, code => str, quantity => int, price => int
# ex) ds_trade_stock('2', 'A005930', 1, 64000)
def ds_trade_stock(buysell, code, quantity, price):

    # 주문 초기화
    initCheck = instCpTdUtil.TradeInit(0)
    if (initCheck != 0):
        print('주문 초기화 실패, 연결 상태 확인 필요')
        return


    # # 주식 매수 주문
    acc = instCpTdUtil.AccountNumber[0] #계좌번호
    accFlag = instCpTdUtil.GoodsList(acc, 1)  # 주식상품 구분

    instCpTd0311.SetInputValue(0, buysell)   # 1: 매도, 2: 매수
    instCpTd0311.SetInputValue(1, acc )   #  계좌번호
    instCpTd0311.SetInputValue(2, accFlag[0])   # 상품구분
    instCpTd0311.SetInputValue(3, code)   # 종목코드
    instCpTd0311.SetInputValue(4, quantity)   # 매도, 매수 수량
    instCpTd0311.SetInputValue(5, price)   # 주문단가
    instCpTd0311.SetInputValue(7, '0')   # 주문 조건 구분 코드, 0: 기본 1: IOC 2:FOK
    instCpTd0311.SetInputValue(8, '01')   # 주문호가 구분코드 - 01: 보통

    # 매수 주문 요청
    nRet = instCpTd0311.BlockRequest()
    if (nRet != 0) :
        print('주문요청 오류', nRet)    
        # 0: 정상,  1: 통신요청 실패, 2: 주문확인창에서 취소, 3: 그외의 내부 오류, 4: 주문요청제한 개수 초과 
    else:
        print('주문 정상 접수')

    rqStatus = instCpTd0311.GetDibStatus() # Dib Server 상태 확인
    errMsg = instCpTd0311.GetDibMsg1() # 확인 메시지 출력
    if rqStatus != 0:
        print('Dib 연결 실패 : ', rqStatus, errMsg)

def ds_account_stock_check():
# 주문 초기화
    initCheck = instCpTdUtil.TradeInit(0)
    if (initCheck != 0):
        print('주문 초기화 실패, 연결 상태 확인 필요')
        return
    
    rqStatus = instCpTd6033.GetDibStatus() # Dib Server 상태 확인
    errMsg = instCpTd6033.GetDibMsg1() # 확인 메시지 출력
    if rqStatus != 0:
        print('Dib 연결 실패 : ', rqStatus, errMsg)
    
    acc = instCpTdUtil.AccountNumber[0]  # 계좌번호
    accFlag = instCpTdUtil.GoodsList(acc, 1)  # 주식상품 구분

    instCpTd6033.SetInputValue(0, acc)
    instCpTd6033.SetInputValue(1, accFlag[0])
    instCpTd6033.SetInputValue(2, 50) # 요청 갯수(최대 50)

    instCpTd6033.BlockRequest()

    cnt = instCpTd6033.GetHeaderValue(7)

    code_list = []

    for i in range(cnt):
        print("종목코드 종목명 체결잔고수량 체결장부단가 평가금액 평가손익")
        code = instCpTd6033.GetDataValue(12, i)  # 종목코드
        code_list.append(code)
        name = instCpTd6033.GetDataValue(0, i)  # 종목명
        cashFlag = instCpTd6033.GetDataValue(1, i)  # 신용구분
        date = instCpTd6033.GetDataValue(2, i)  # 대출일
        amount = instCpTd6033.GetDataValue(7, i) # 체결잔고수량
        buyPrice = instCpTd6033.GetDataValue(17, i) # 체결장부단가
        evalValue = instCpTd6033.GetDataValue(9, i) # 평가금액(천원미만은 절사 됨)
        evalPerc = instCpTd6033.GetDataValue(11, i) # 평가손익

        print(code, name, amount, buyPrice, evalValue, evalPerc)
    
    return code_list
    
    
    
#################################################################################################
# Investing Data 생성, 1회 실행 후 추가 실행 필요 없음
#################################################################################################

sqlalchemy_conn = sqlalchemy_connect_ip('192.168.50.123', 'investing_data')
investing_data_list = get_pymysql_db_list(sqlalchemy_conn, 'investing_data')
investing_df = get_investing_data(sqlalchemy_conn, investing_data_list)

#################################################################################################


# 실시간 감시 종목
# while True:

target_df = pd.DataFrame()
for code in stock_list:
    
    day_stock_investing_df = get_pymysql_day_stock(sqlalchemy_conn, code, yesterday, investing_df)
    each_target_df = get_realtime_stock_info(code, today)
    each_target_df = pd.concat([each_target_df, day_stock_investing_df], axis=1)
    target_df = pd.concat([target_df, each_target_df], axis=0)

try:
    ds_account_stock_check() # 잔고 조회
except:
    print('현재 보유 중인 주식이 없습니다.')

# 모델 load 영역 #

# 모델 predict 영역 #

# predict 확률로 매수 진행

ds_trade_stock('2', 'A005930', 1, 64000) # 매도 '1', 매수 '2'

    




# 실행 종료 시 DB connection 종료 필요
# sqlalchemy_conn.close()