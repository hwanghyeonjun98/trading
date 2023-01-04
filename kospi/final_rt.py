from final_module.final_target import get_target_list_db_rt
from final_module.final_realtime import realtime_trading, ds_account_db_update
from final_module.final_dbconnect import DBConnection_trading

from pandas.tseries.offsets import BDay
from datetime import date

account_name, account_value = ds_account_db_update(DBConnection_trading().get_sqlalchemy_connect_ip())
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]

# 예측할 종목 설정
kospi_list, kosdaq_list = get_target_list_db_rt()

if (account_name == '01BIG15') | (account_name == '02BIG15') :
    realtime_trading(kosdaq_list, account_name, account_value)   # 소형주  
else:
    realtime_trading(kospi_list, account_name, account_value)  # 대형주