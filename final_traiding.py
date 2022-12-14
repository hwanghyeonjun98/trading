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

from final_dbconnect import *

today = str(date.today()).replace('-','')
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]

## predict 값 DB에 넣기
def stock_tranding(stock_list, investing_df ,col_list ,mode):
    sqlalchemy_conn = DBConnection_trading().get_sqlalchemy_connect_ip()
    sqlalchemy_conn_p = DBConnection_predict().get_sqlalchemy_connect_ip()
    p = pd.DataFrame()
    while True:
        for code in stock_list:
            
            sql = f"SELECT * FROM trading_data.{code}_{today} ORDER BY 시간 DESC LIMIT 1"
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
        
            p.append(predict_df)
            predict_df.to_sql(name='{0}_{1}'.format(code, today), con=sqlalchemy_conn_p, if_exists='replace', index=False)
            
    p.to_csv('../data/')
            
               
            
                
