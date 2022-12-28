from final_dbconnect import DBConnection_trading, DBConnection_predict

from sklearn.preprocessing import MaxAbsScaler
from pandas.tseries.offsets import BDay
from datetime import date, datetime, timedelta
from pickle import load

import pandas as pd
import time


today = str(date.today()).replace('-','')
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]

def get_pymysql_traidng_table_check(table_schema, code, conn, account_name):
    # 현재 DB 내 존재하는 테이블 존재 여부 확인
    sql = f"SELECT count(*) FROM Information_schema.tables  WHERE table_schema = '{table_schema}' AND table_name = '{account_name}_{today}_{code}'"

    cur = conn.cursor()
    count = cur.execute(sql)
    conn.close()

    return count

def get_pymysql_day_stock(conn, code, yesterday, investing_df):

    code = code[-6:]
    sql = f"SELECT 전일대비, 상장주식수, 시가총액, 외국인현보유수량, 외국인현보유비율, 기관순매수량, 기관누적순매수량, 년, 월, 일 FROM stock_info.`{code}` WHERE 날짜={yesterday} ORDER BY 시간 DESC LIMIT 1"
    
    result = conn.execute(sql)

    target_df = pd.DataFrame(result.fetchall())
    # target_df.set_index('날짜', inplace=True)
    # target_df.rename(index={int(yesterday):today}, inplace=True)
    target_df = pd.concat([target_df, investing_df], axis=1)
    conn.close()

    return target_df

## predict 값 DB에 넣기
def stock_predict(stock_list, investing_df, col_list,  model, account_name):

    account_name = account_name.lower()
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
                   
            for code in stock_list:
                
                today = str(date.today()).replace('-','')
                yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]

                cnt = 0
                count = 0
                while True:
                    cnt += 1
                    if cnt == 10:
                        print('진행중~~~~~~~')
                        cnt = 0
                    count = get_pymysql_traidng_table_check('trading_data',code, DBConnection_trading().get_pymysql_connection(), account_name)
                    if count == 1:
                        break
                    time.sleep(1)
                # 전날 일봉 데이터와 investing data
                day_stock_investing_df = get_pymysql_day_stock(DBConnection_trading().get_sqlalchemy_connect_ip(), code, yesterday, investing_df)
                
                # day_stock_investing_df.reset_index(drop=True, inplace=True)
                try:
                    sql = f"SELECT 시간, 시가, 고가, 저가, 종가, 거래량, 거래대금, 누적체결매도수량, 누적체결매수수량, 년, 월, 일 FROM trading_data.`{account_name}_{today}_{code}` ORDER BY 시간 DESC LIMIT 1"
                    table_data = DBConnection_trading().get_sqlalchemy_connect_ip().execute(sql) 
                except:
                    print('SQL 조회 에러 발생')
                
                try:
                    table_df = pd.DataFrame(table_data.fetchall())  # DB내 테이블을 DF로 변환
                    table_df = pd.concat([table_df, day_stock_investing_df], axis=1 )
                    table_df = table_df.apply(pd.to_numeric)
                    
                    c_list = list(col_list.index)
                    
                    each_target_df = table_df[c_list]
                except:
                    print('trading_df 추출 에러')
                    
                try:
                    # min_abs_scaler = MaxAbsScaler()
                    try:
                        min_abs_scaler = load(open(f'./download/scaler/{yesterday}_scaler', 'rb'))
                        
                        X_pred_sc = min_abs_scaler.transform(each_target_df)
                        X_pred = X_pred_sc.reshape(X_pred_sc.shape[0], model.input.shape[1], 1)
                        
                        predict = model.predict(X_pred)
                    except:
                        temp_day=str(date.today() - timedelta(1)).replace('-','').split(' ')[0]
                        min_abs_scaler = load(open(f'./download/scaler/{temp_day}_scaler', 'rb'))
                        X_pred_sc = min_abs_scaler.transform(each_target_df)
                        X_pred = X_pred_sc.reshape(X_pred_sc.shape[0], model.input.shape[1], 1)
                        
                        predict = model.predict(X_pred)
                except:
                    print('scaler 에러')
                try:
                    predict_df = pd.DataFrame(predict)
                    predict_df['비교'] = (predict_df[0] - predict_df[1])
                    predict_df['id'] = t
                    predict_df['시간'] = str(now.hour) + ':' + str(now.minute)

                except:
                    print('predict dataframe 에러')
                
                try:
                    pred_cnt =  get_pymysql_traidng_table_check('predict_data',code, DBConnection_trading().get_pymysql_connection(), account_name)
                    time.sleep(0.2)
                    if pred_cnt == 0:
                        predict_df.to_sql(name=f'{account_name}_{today}_{code}', con=DBConnection_predict().get_sqlalchemy_connect_ip(), if_exists='replace', index=False)
                        
                    else:
                        predict_df.to_sql(name=f'{account_name}_{today}_{code}', con=DBConnection_predict().get_sqlalchemy_connect_ip(), if_exists='append', index=False)
                except:
                    print('predict 에러')

        
            
               
            
                
