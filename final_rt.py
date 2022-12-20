from final_target import *
from final_realtime import realtime_trading

# 예측할 종목 설정
kospi_list, kosdaq_list = get_target_list_db()
investing_df = get_target(path=r'D:\systrader-dev\trading\download\target')

realtime_trading(kosdaq_list, investing_df)