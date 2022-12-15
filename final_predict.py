from datetime import date, datetime
from pandas.tseries.offsets import BDay
from sklearn.preprocessing import MaxAbsScaler
import pandas as pd
import time

from final_realtime import get_pymysql_db_table_check
from final_dbconnect import *

today = str(date.today()).replace('-','')
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]


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
def stock_predict(stock_list, col_list, investing_df, model):

    pred_df = pd.DataFrame()
    while True:
        now = datetime.now()
        if (now.minute > 30) & (now.hour >= 15):
            break
        elif (now.hour < 9):
            time.sleep(1)
        else:          
            for code in stock_list:
                while True:
                    count = get_pymysql_db_table_check('trading_data', code, DBConnection_trading().get_sqlalchemy_connect_ip())
                    if count == 1:
                        break
                    time.sleep(1)
                # 전날 일봉 데이터와 investing data
                day_stock_investing_df = get_pymysql_day_stock(DBConnection_trading().get_sqlalchemy_connect_ip(), code, yesterday, investing_df)
                 
                sql = f"SELECT * FROM trading_data.{code}_{today} ORDER BY 시간 DESC LIMIT 1"
                table_data = DBConnection_trading().get_sqlalchemy_connect_ip().execute(sql) 
                table_df = pd.DataFrame(table_data.fetchall())  # DB내 테이블을 DF로 변환
                
                 #  (전날 일봉 데이터와 investing data) + 업데이트 데이터
                table_df = pd.concat([table_df, day_stock_investing_df], axis=1)
                
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
            
               
            
                
