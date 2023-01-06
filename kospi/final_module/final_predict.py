from final_module.final_dbconnect import DBConnection_trading, DBConnection_predict

from sklearn.preprocessing import MaxAbsScaler
from pandas.tseries.offsets import BDay
from datetime import date, datetime, timedelta
from pickle import load

import pandas as pd
import time


today = str(date.today()).replace('-','')
yesterday = str(date.today() - BDay(1)).replace('-','').split(' ')[0]
temp_day = str(date.today() - timedelta(1)).replace('-','').split(' ')[0] # timedelta : 전체 일자 -> 하루 뒤

# 현재 DB 내 존재하는 테이블 존재 여부 확인 
def get_pymysql_traidng_table_check(table_schema, code, conn, account_name):
    sql = f"SELECT count(*) FROM Information_schema.tables  WHERE table_schema = '{table_schema}' AND table_name = '{account_name}_{today}_{code}'"

    cur = conn.cursor()
    count = cur.execute(sql)
    conn.close()

    return count # 존재하는 테이블 갯수 반환

# 전일 일봉 데이터 불러오기 
def get_pymysql_day_stock(conn, code, yesterday, investing_df):

    code = code[-6:]
    sql = f"SELECT 전일대비, 상장주식수, 시가총액, 외국인현보유수량, 외국인현보유비율, 기관순매수량, 기관누적순매수량, 년, 월, 일 FROM stock_info.`{code}` WHERE 날짜={yesterday} ORDER BY 시간 DESC LIMIT 1"
    
    result = conn.execute(sql)

    target_df = pd.DataFrame(result.fetchall())

    target_df = pd.concat([target_df, investing_df], axis=1)
    conn.close()

    return target_df


###############################################################################################################################################################################
###############################################################################################################################################################################

## predict 값 DB에 넣기
def stock_predict(stock_list, investing_df, col_list,  model, account_name):

    account_name = account_name.lower() # 소문자로 변환
    time_cnt = 0
   
    while True:        
        now = datetime.now()
        t = time.time()

        if (now.minute == 30) & (now.hour == 15):
            break

        elif (now.hour < 9) | (now.hour > 16):
            time_cnt += 1
            if time_cnt == 10:
                print('박대기중~~~~~~~')
                time_cnt = 0
            time.sleep(1)

        else:
            for code in stock_list: # 대형주 : kospi_list,  소형주 : kosdaq_list
            
                cnt = 0
                count = 0
                while True:
                    cnt += 1
                    if cnt == 10:
                        print('진행중~~~~~~~')
                        cnt = 0
                    # 테이블 존재 여부 확인 -> 테이블 : 각 종목별 실시간 데이터
                    count = get_pymysql_traidng_table_check('trading_data',code, DBConnection_trading().get_pymysql_connection(), account_name)
                    # count = 1 테이블이 존재함
                    if count == 1:
                        break
                    time.sleep(1)

                # 전날 일봉 데이터와 investing data 합치기
                day_stock_investing_df = get_pymysql_day_stock(DBConnection_trading().get_sqlalchemy_connect_ip(), code, yesterday, investing_df)

                try:
                    # DB 내 존재하는 실시간 데이터 추출
                    sql = f"SELECT 시간, 시가, 고가, 저가, 종가, 거래량, 거래대금, 누적체결매도수량, 누적체결매수수량 FROM trading_data.`{account_name}_{today}_{code}` ORDER BY 시간 DESC LIMIT 1"
                    table_data = DBConnection_trading().get_sqlalchemy_connect_ip().execute(sql) 
                except:
                    print('SQL 조회 에러 발생')
                
                try:
                    # 데이터 프레임으로 생성
                    table_df = pd.DataFrame(table_data.fetchall())  # DB내 테이블을 DF로 변환
                    
                    # 실시간 데이터와 전일 데이터를 concat
                    table_df = pd.concat([table_df, day_stock_investing_df], axis=1 )
                    table_df = table_df.apply(pd.to_numeric)
                    # 상관계수가 높은 컬럼만 추출
                    c_list = list(col_list.index)
                    each_target_df = table_df[c_list]
                  

                except:
                    print('trading_df 추출 에러')
                    
                try:
                    try:
                        # 학습 시 사용한 스케일러 호출
                        min_abs_scaler = load(open(f'./download/scaler/{yesterday}_scaler', 'rb'))
                        X_pred_sc = min_abs_scaler.transform(each_target_df)
                        # 학습 데이터와 차원 맞추기
                        X_pred = X_pred_sc.reshape(X_pred_sc.shape[0], model.input.shape[1], 1)
                        predict = model.predict(X_pred)
                    except:
                        min_abs_scaler = load(open(f'./download/scaler/{temp_day}_scaler', 'rb'))
                        X_pred_sc = min_abs_scaler.transform(each_target_df)
                        X_pred = X_pred_sc.reshape(X_pred_sc.shape[0], model.input.shape[1], 1)
                        predict = model.predict(X_pred)
                except:
                    print('scaler 에러')
                try:
                    predict_df = pd.DataFrame(predict)
                    predict_df['비교'] = (predict_df[0] - predict_df[1]) # 비율 확인
                    predict_df['id'] = t # order by 하기 위해서
                    predict_df['시간'] = str(now.hour) + ':' + str(now.minute) # 시간 확인

                except:
                    print('predict dataframe 에러')
                
                try:
                    # 테이블 존재 여부 확인 
                    pred_cnt =  get_pymysql_traidng_table_check('predict_data',code, DBConnection_trading().get_pymysql_connection(), account_name)
                    time.sleep(0.2)
                    # 테이블 없으면 replace로 새로 만들고
                    if pred_cnt == 0:
                        predict_df.to_sql(name=f'{account_name}_{today}_{code}', con=DBConnection_predict().get_sqlalchemy_connect_ip(), if_exists='replace', index=False)
                    # 있으면 append 해라
                    else:
                        predict_df.to_sql(name=f'{account_name}_{today}_{code}', con=DBConnection_predict().get_sqlalchemy_connect_ip(), if_exists='append', index=False)
                except:
                    print('predict 에러')

        
            
               
            
                
