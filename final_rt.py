from final_target import get_target_list_db
from final_realtime import realtime_trading

from pandas.tseries.offsets import BDay
from datetime import date
import pandas as pd


yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0]

# 예측할 종목 설정
kospi_list, kosdaq_list = get_target_list_db()
investing_df = pd.read_csv(f'./download/investing_df/investing_{yesterday}.csv', encoding='utf-8-sig', index_col=0)

realtime_trading(kosdaq_list, investing_df)