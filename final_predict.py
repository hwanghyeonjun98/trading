from datetime import date, datetime
from pandas.tseries.offsets import BDay
from sklearn.preprocessing import MaxAbsScaler
import pandas as pd
import time

# from final_realtime import get_pymysql_db_table_check
from final_dbconnect import *

today = str(date.today()).replace('-','')
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]

def get_pymysql_traidng_table_check(code, conn):
    # 현재 DB 내 존재하는 테이블 존재 여부 확인
    sql = f"SELECT 1 FROM Information_schema.tables  WHERE table_schema = 'trading_data' AND table_name = '{code}_{today}'"

    cur = conn.cursor()
    count = cur.execute(sql)

    return count

def get_pymysql_day_stock(conn, code, yesterday, investing_df):

    code = code[-6:]
    sql = f"SELECT 전일대비, 상장주식수, 시가총액, 외국인현보유수량, 외국인현보유비율, 기관순매수량, 기관누적순매수량, 년, 월, 일 FROM stock_info.`{code}` WHERE 날짜={yesterday} ORDER BY 시간 DESC LIMIT 1"
    
    result = conn.execute(sql)

    target_df = pd.DataFrame(result.fetchall())
    # target_df.set_index('날짜', inplace=True)
    # target_df.rename(index={int(yesterday):today}, inplace=True)
    target_df = pd.concat([target_df, investing_df], axis=1)

    return target_df

## predict 값 DB에 넣기
def stock_predict(stock_list, investing_df, col_list,  model):

    pred_df = pd.DataFrame()
    time_cnt = 0
    while True:
        now = datetime.now()
        if (now.minute > 30) & (now.hour >= 15):
            break
        elif (now.hour < 9) | (now.hour > 16):
            time_cnt += 1
            if time_cnt == 10:
                print('박대기중~~~~~~~')
                time_cnt = 0
            time.sleep(1)
        else:          
            for code in stock_list:
                cnt = 0
                while True:
                    cnt += 1
                    if cnt == 10:
                        print('진행중~~~~~~~')
                        cnt = 0
                    count = get_pymysql_traidng_table_check(code, DBConnection_trading().get_pymysql_connection())
                    if count == 1:
                        break
                    time.sleep(1)
                # 전날 일봉 데이터와 investing data
                
                day_stock_investing_df = get_pymysql_day_stock(DBConnection_trading().get_sqlalchemy_connect_ip(), code, yesterday, investing_df)
                
                # day_stock_investing_df.reset_index(drop=True, inplace=True)
                sql = f"SELECT * FROM trading_data.{code}_{today} ORDER BY 시간 DESC LIMIT 1"
                table_data = DBConnection_trading().get_sqlalchemy_connect_ip().execute(sql) 
                table_df = pd.DataFrame(table_data.fetchall())  # DB내 테이블을 DF로 변환
                
            
                table_df = pd.concat([table_df, day_stock_investing_df], axis=1 )
                
                c_list = list(col_list.index)
                table_df = table_df.set_index(['날짜'])
                each_target_df = table_df[c_list]
                min_abs_scaler = MaxAbsScaler()
                X_pred_sc = min_abs_scaler.fit_transform(each_target_df)
                X_pred = X_pred_sc.reshape(X_pred_sc.shape[0], model.input.shape[1], 1)
            
                predict = model.predict(X_pred )
                
                predict_df = pd.DataFrame(predict)
            
                pred_df.append(predict_df)
                
                predict_df.to_sql(name='{0}_{1}'.format(code, today), con=DBConnection_predict().get_sqlalchemy_connect_ip(), if_exists='replace', index=False)
                
    pred_df.to_csv(f'./download/predict_df/{code}_{today}', encoding='utf-8-sig')
            
               
            
                
