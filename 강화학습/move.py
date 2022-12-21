import shutil
import os
import time

if not os.path.isdir('./output/6_month'):
    os.makedirs('./output/6_month')

shutil.move('./models/005930_a3c_lstm_policy.mdl', './output/6_month')
shutil.move('./models/005930_a3c_lstm_value.mdl', './output/6_month')
shutil.move('./output/train_005930_a3c_lstm', './output/6_month')
time.sleep(300)