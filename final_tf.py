from final_model import *
from final_db_update import *
from final_realtime import *
from final_predict import *
from final_target import *

from keras.models import load_model
import tensorflow as tf

# tf gpu 메모리 관련 코드 
gpus = tf.config.list_physical_devices(device_type = 'GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

kospi_list, kosdaq_list, investing_df = get_target(path=r'D:\systrader-dev\trading\download\target')

# # 대형주 1년 학습
# ls_big_year = LstmNetwork('대형주', kospi_list, '1년', 280, 0.02)
# col_list_big_year = ls_big_year.complete_corr
# modelpath_big_year = ls_big_year.LstmModel()
# model_big_year = load_model(modelpath_big_year)

# # 대형주 1년 트레이딩
# stock_predict(kospi_list, investing_df, col_list_big_year, model_big_year)



# # 대형주 6개월 학습
# ls_big_six_month = LstmNetwork('대형주', kospi_list, '6개월', 140, 0.04 )
# col_list_big_six_month = ls_big_six_month.complete_corr
# modelpath_big_six_month = ls_big_six_month.LstmModel()
# model_big_six_month = load_model(modelpath_big_six_month)

# # 대형주 6개월 트레이딩
# stock_predict(kospi_list, investing_df, col_list_big_six_month, model_big_six_month)



# # 소형주 1년 학습
# ls_small_year = LstmNetwork('소형주', kosdaq_list, '1년', 280, 0.03)
# col_list_small_year = ls_small_year.complete_corr
# modelpath_small_year = ls_small_year.LstmModel()
# model_small_year = load_model(modelpath_small_year)

# # 소형주 1년 트레이딩
# stock_predict(kosdaq_list, investing_df, col_list_small_year, model_small_year)



# 소형주 6개월 학습
ls_small_six_month = LstmNetwork('소형주', kosdaq_list, '6개월', 140, 0.03)
col_list_small_six_month = ls_small_six_month.complete_corr
modelpath_small_six_month = ls_small_six_month.LstmModel()
model_small_six_month = load_model(modelpath_small_six_month)

# 소형주 6개월 트레이딩
stock_predict(kosdaq_list, investing_df, col_list_small_six_month, model_small_six_month)






# if __name__ == "__main__":
#     traiding_start()