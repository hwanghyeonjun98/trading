# [종목명 리스트]
def get_stock_list():
    count = instCpStockCode.GetCount()
    stock_list = []
    
    for i in range(count):
        stock_list.append(instCpStockCode.GetData(1,i))
    
    return stock_list


# 코드, 종목명 분리 => []로 추출
def get_code_name_list():
    codelist = instCpCodeMgr.GetStockListByMarket(1)
    code_name_list = [] 
    code_list = []
    for i, code in enumerate(codelist):
        secondCode = instCpCodeMgr.GetStockSectionKind(code)
        name = instCpCodeMgr.CodeToName(code)
        code_list.append(code)
        code_name_list.append(name)


# 코스피 가져오기 => { 코드 : 종목명}
def get_kospy():
    codelist = instCpCodeMgr.GetStockListByMarket(1)
    kospi = {}
    for code in codelist:
        name = instCpCodeMgr.CodeToName(code)
        kospi[code] = name

        
        

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

        
