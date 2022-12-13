
from final_model import *
from final_db_update import *
from realtime_traiding import *

# tf gpu 메모리 관련 코드 
gpus = tf.config.list_physical_devices(device_type = 'GPU')
tf.config.experimental.set_memory_growth(gpus[0], True)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

db_list_update(computer_name='user')


big_stock_table_list = ['005930','373220','207940','000660','051910','247540','091990','066970','293490','028300'] # 대형주
small_stock_table_list = ['016790','095500','205470','278650','151860','053690','117580','063080','027710','011700'] # 소형주


ls = LstmNetwork('대형주', big_stock_table_list, '6개월', 140, 0.02)




class final():
    def __init__(self):
        
        self.modelpath = ls.LstmModel(complete_df)