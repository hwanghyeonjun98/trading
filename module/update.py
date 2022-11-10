from module.setting import instCpCodeMgr

import pandas as pd
import re



# 코드명이 A로 시작하는 것만 추출
def update_stock_list():
        stock_list = []
        stock_list = stock_list + list(instCpCodeMgr.GetStockListByMarket(2))
        stock_list_real = []
        p = re.compile('^A')

        for stock in stock_list:
                if p.match(str(stock)) != None:
                        stock_list_real.append(stock)
        return stock_list_real
                    
                