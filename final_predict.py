from datetime import date
from pandas.tseries.offsets import BDay
from sklearn.preprocessing import MaxAbsScaler
import pandas as pd


from final_dbconnect import *

today = str(date.today()).replace('-','')
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]

## predict 값 DB에 넣기
def stock_predict(stock_list,col_list ,model):
    sqlalchemy_conn = DBConnection_trading().get_sqlalchemy_connect_ip()
    sqlalchemy_conn_p = DBConnection_predict().get_sqlalchemy_connect_ip()
    p = pd.DataFrame()
    for i in range(10):    # while True:
        for code in stock_list:
            
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
        
            p.append(predict_df)
            predict_df.to_sql(name='{0}_{1}'.format(code, today), con=sqlalchemy_conn_p, if_exists='replace', index=False)
    p.to_csv('../data/')
            
               
            
                
