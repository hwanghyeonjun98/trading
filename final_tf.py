from final_target import get_target_list_db
from final_model import LstmNetwork
from datetime import date

import pandas as pd
import tensorflow as tf
import os


# tf gpu 메모리 관련 코드 
gpus = tf.config.list_physical_devices(device_type = 'GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

today = str(date.today()).replace('-','')
investing_df =  pd.read_csv(f'./download/investing_df/investing_{today}.csv', encoding='utf-8-sig', index_col=0) # 각자 컴퓨터의 맞게 변경
kospi_list, kosdaq_list = get_target_list_db()
# C:\big15\project-dev\trading\download\target
# D:\systrader-dev\trading\download\target


# # 대형주 1년 학습
# ls_big_year = LstmNetwork('대형주', kospi_list, '1년', 280, 0.02)

# # 대형주 6개월 학습
# ls_big_six_month = LstmNetwork('대형주', kospi_list, '6개월', 140, 0.04 )

# # 소형주 1년 학습
# ls_small_year = LstmNetwork('소형주', kosdaq_list, '1년', 280, 0.03)

# 소형주 6개월 학습
ls_small_six_month = LstmNetwork('소형주', kosdaq_list, '6개월', 140, 0.03)