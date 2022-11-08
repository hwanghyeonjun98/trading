from module.setting import instCpStockCode, instCpCodeMgr, instStockChart
import pandas as pd
import os

# [종목명 리스트] : 코스피+ 코스닥
def get_stock_list():
    
    count = instCpStockCode.GetCount()
    stock_list = []
    
    for i in range(count):
        stock_list.append(instCpStockCode.GetData(1,i))
    
    return stock_list


# 코스피 가져오기 => { 코드 : 종목명}
def get_kospy():
    codelist = instCpCodeMgr.GetStockListByMarket(1)
    kospi = {}
    for code in codelist:
        name = instCpCodeMgr.CodeToName(code)
        kospi[code] = name
        
    return kospi


# 코드 []로 추출 : 코스피
def get_code_list():
    code_list = list(instCpCodeMgr.GetStockListByMarket(1) + instCpCodeMgr.GetStockListByMarket(2))

    return code_list
  
        

# 종목명 []로 추출 : 코스피
def get_name_list():
    codelist = instCpCodeMgr.GetStockListByMarket(1)
    code_name_list = [] 
    for code in codelist:
        name = instCpCodeMgr.CodeToName(code)
        code_name_list.append(name)
        
    return code_name_list

# 코스피, 코스닥 수집 안된 리스트 가져오기(네트워크 경로 기반)
def get_empty_list():
    current_list = []

    for list in os.listdir(r'\\DESKTOP-H2H6JNB\data):
        current_list.append('A'+list.split('_')[0])

    current_set = set(current_list)
    empty_list = [x for x in get_code_list() if x not in current_set]
    
    return empty_list

# 특정 범위 일자 종목 데이터 가져오기   
def get_stock_info(stock_code, start_day, end_day, type):
    
    instStockChart.SetInputValue(0, stock_code) # 종목명
    instStockChart.SetInputValue(1, ord('1')) # 1 : 기간으로 요청, 2: 개수로 요청
    instStockChart.SetInputValue(3, start_day) # 요청 시작일
    instStockChart.SetInputValue(2, end_day) # 요청 종료일
    # instStockChart.SetInputValue(4, request_num) # 요청 개수
    '''
    # 요청할 데이터 종류(리스트 형태로 요청 가능)
    0 : 날짜, 1 : 시간 - hhmm, 2 : 시가, 3 : 고가, 4 : 저가, 5 : 종가
    6 : 전일대비, 8 : 거래량, 9 : 거래대금, 13 : 시가총액
    '''
    instStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17,18, 19,20,21,22,23,24,25,26])
    instStockChart.SetInputValue(6, ord(type)) # 'D' : 일봉, 'm' : 분봉
    instStockChart.SetInputValue(9, ord('1'))

    instStockChart.BlockRequest() # 위 정보로 요청

    numrow, numcolumn = instStockChart.GetHeaderValue(3), instStockChart.GetHeaderValue(2)

    index = []
    for i in range(numrow):
        index_ = str(instStockChart.GetDataValue(0,i))
        index.append(index_)

    stock_info = pd.DataFrame(columns=numcolumn[1:], index=index)

    for num in range(numrow):
        for col in range(len(numcolumn)):
            # 1,2,3,4,5,6,7,8,9, 10
            stock_info.iloc[num, col-1] = str(instStockChart.GetDataValue(col,num))
    
    return stock_info

        
