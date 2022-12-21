from final_target import get_target_list_db, get_target
from final_predict import stock_predict
from final_model import LstmNetwork

import tensorflow as tf
import os


# tf gpu 메모리 관련 코드 
gpus = tf.config.list_physical_devices(device_type = 'GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


kospi_list, kosdaq_list = get_target_list_db()
investing_df = get_target(path=r'D:\systrader-dev\trading\download\target') # 각자 컴퓨터의 맞게 변경
# C:\big15\project-dev\trading\download\target
# D:\systrader-dev\trading\download\target


# # 대형주 1년 학습
# account_name= '04BIG15'
# ls_big_year = LstmNetwork('대형주', kospi_list, '1년', 280, 0.02)
# col_list_big_year = ls_big_year.col_list
# model_big_year = ls_big_year.model_weight

# # 대형주 1년 트레이딩
# stock_predict(kospi_list, investing_df, col_list_big_year, model_big_year, account_name)



# # 대형주 6개월 학습
# account_name= '03BIG15'
# ls_big_six_month = LstmNetwork('대형주', kospi_list, '6개월', 140, 0.04 )
# col_list_big_six_month = ls_big_six_month.col_list
# model_big_six_month = ls_big_six_month.model_weight

# # 대형주 6개월 트레이딩
# stock_predict(kospi_list, investing_df, col_list_big_six_month, model_big_six_month, account_name)



# # 소형주 1년 학습
# account_name= '02BIG15'
# ls_small_year = LstmNetwork('소형주', kosdaq_list, '1년', 280, 0.03)
# col_list_small_year = ls_small_year.col_list
# model_small_year = ls_small_year.model_weight

# # 소형주 1년 트레이딩
# stock_predict(kosdaq_list, investing_df, col_list_small_year, model_small_year, account_name)



# 소형주 6개월 학습
account_name= '01BIG15'
ls_small_six_month = LstmNetwork('소형주', kosdaq_list, '6개월', 140, 0.03)
col_list_small_six_month = ls_small_six_month.col_list
model_small_six_month = ls_small_six_month.model_weight

# with open( './pickle/pickle_corr_complete/소형주_20221216_6개월_10개_0.03.pkl', 'rb') as p:
#     col_list_small_six_month = pickle.load(p)
# modelpath_small_six_month = './model/소형주_20221216_6개월_lstm_30ep_64bs_5pa_0.03newcor.hdf5'
# model_small_six_month = load_model(modelpath_small_six_month)

# 소형주 6개월 트레이딩
stock_predict(kosdaq_list, investing_df, col_list_small_six_month, model_small_six_month, account_name)