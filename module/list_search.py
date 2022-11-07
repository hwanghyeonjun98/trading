# 종목 이름 => [코드, 종목명]
def search_by_name(stock_name):
    count = instCpStockCode.GetCount()
    for i in range(count):
        if instCpStockCode.GetData(1,i) == stock_name:
            # GetData(x,y)
            # x : 0 => 종목 코드
            # x : 1 => 종목명
            # x : 2 => ISIN 코드(ISIN : 국제 증권 식별 번호)
            return [instCpStockCode.GetData(0,i), instCpStockCode.GetData(1,i)]
        
# 특정 코드 => [코드, 종목명]      
def search_by_code(stock_code):
    count = instCpStockCode.GetCount()
    for i in range(count):
        if instCpStockCode.GetData(0,i) == stock_code:
            # GetData(x,y)
            # x : 0 => 종목 코드
            # x : 1 => 종목명
            # x : 2 => ISIN 코드(ISIN : 국제 증권 식별 번호)
            return [instCpStockCode.GetData(0,i), instCpStockCode.GetData(1,i)]
