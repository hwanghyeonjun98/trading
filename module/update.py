# 코드명이 A로 시작하는 것만 추출
def update_stock_list():
    stock_list = []
    stock_list = stock_list + list(instCpCodeMgr.GetStockListByMarket(2))
    stock_list_real = []
    p = re.compile('^A')

    for stock in stock_list:
            if p.match(str(stock)) != None:
                    stock_list_real.append(stock)
                    
                    
# 분봉 일봉 데이터 불러와서 분봉 빈칸 일봉으로 채우기
def update_min_day_concat():
    files_m = os.listdir('../data')
    files_d = os.listdir('../data_day') 
    
    for j, (min_df, day_df) in enumerate(zip(files_m, files_d)):
      globals()[f'data_m{j}'] = pd.read_csv(f'../data/{min_df}', index_col='Unnamed: 0')
      globals()[f'data_d{j}'] = pd.read_csv(f'../data_day/{day_df}', index_col='Unnamed: 0')
      
      for v in tqdm(globals()[f'data_m{j}'].index):
            input_list = ['전일대비','상장주식수','시가총액','외국인주문한도수량'
                    ,'외국인주문가능수량','외국인현보유수량','외국인현보유비율'
                    ,'수정주가일자','수정주가비율','기관순매수량','기관누적순매수량']
            
            globals()[f'data_m{j}'].loc[v, input_list] = globals()[f'data_d{j}'].loc[v, input_list].values
           