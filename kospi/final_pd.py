from final_module.final_target import get_target_list_db_rt
from final_module.final_predict import stock_predict

from pandas.tseries.offsets import BDay
from keras.models import load_model
from datetime import date, timedelta

import tensorflow as tf
import pandas as pd
import pickle
import os

# tf gpu 메모리 관련 코드 P
gpus = tf.config.list_physical_devices(device_type = 'GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

account_name= '03big15' # 계좌명 입력
yesterday=str(date.today() - BDay(1)).replace('-','').split(' ')[0] # 비지니스 데이로 어제 날짜
temp_day=str(date.today() - timedelta(1)).replace('-','').split(' ')[0] # 일반 어제 날짜

today = str(date.today()).replace('-','')
kospi_list, kosdaq_list = get_target_list_db_rt()

try:
    investing_df =  pd.read_csv(f'./download/investing_df/investing_{yesterday}.csv', encoding='utf-8-sig', index_col=0)    
    
    with open(f'./pickle/pickle_corr_complete/대형주_{yesterday}_6개월_10개_0.04.pkl', 'rb') as f:
        col_list_big_six_month = pickle.load(f) # 상관 계수에 따른 컬럼 리스트
    model_big_six_month = load_model(f"./model/weight/대형주_{yesterday}_6개월_lstm_30ep_64bs_5pa_0.04newcor.hdf5")

except:
    investing_df =  pd.read_csv(f'./download/investing_df/investing_{temp_day}.csv', encoding='utf-8-sig', index_col=0)    
    
    with open(f'./pickle/pickle_corr_complete/대형주_{temp_day}_6개월_10개_0.04.pkl', 'rb') as f:
        col_list_big_six_month = pickle.load(f) # 상관 계수에 따른 컬럼 리스트
    model_big_six_month = load_model(f"./model/weight/대형주_{temp_day}_6개월_lstm_30ep_64bs_5pa_0.04newcor.hdf5")


# 대형주 6개월 트레이딩
stock_predict(kospi_list, investing_df, col_list_big_six_month, model_big_six_month, account_name)