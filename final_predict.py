from datetime import date, datetime
from pandas.tseries.offsets import BDay
from sklearn.preprocessing import MaxAbsScaler
import pandas as pd
import time

from final_realtime import get_pymysql_db_table_check
from final_dbconnect import *

today = str(date.today()).replace('-','')
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]

## predict 값 DB에 넣기
def stock_predict(stock_list,col_list ,model):
    sqlalchemy_conn = DBConnection_trading().get_sqlalchemy_connect_ip()
    sqlalchemy_conn_p = DBConnection_predict().get_sqlalchemy_connect_ip()
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
                
                sql = f"SELECT * FROM predict_data.{code}_{today} ORDER BY 시간 DESC LIMIT 1"
                table_data = sqlalchemy_conn.execute(sql) 
                table_df = pd.DataFrame(table_data.fetchall())  # DB내 테이블을 DF로 변환
                
                c_list = list(col_list.index)
                table_df = table_df.set_index(['날짜'])
                each_target_df = table_df[c_list]
                min_abs_scaler = MaxAbsScaler()
                X_pred_sc = min_abs_scaler.fit_transform(each_target_df)
                X_pred = X_pred_sc.reshape(X_pred_sc.shape[0], model.input.shape[1], 1)
                
                predict = model.predict(X_pred )
                
                predict_df = pd.DataFrame(predict)
            
                pred_df.append(predict_df) 
                predict_df.to_sql(name='{0}_{1}'.format(code, today), con=sqlalchemy_conn_p, if_exists='replace', index=False)
                
    pred_df.to_csv(f'./download/predict_df/{code}_{today}', encoding='utf-8-sig')
            
               
            
                
