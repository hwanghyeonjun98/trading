from module.dir import dir_min_open, dir_day_open, dir_min_update_open
from module.dir import dir_day_update_open, dir_concat_open
from module.dir import dir_min_update_save, dir_day_update_save
from module.dir import dir_concat_save,dir_label_save
from module.dir import file_min, file_day, file_min_update, file_day_update, file_concat

from module.setting import instCpCybos
from module.search import search_by_code
from module.get import get_stock_info
from module.update import update_stock_list

from tqdm import tqdm
from datetime import datetime
from datetime import timedelta
import pandas as pd
import time
import os


# 파일 경로 설정 후 오픈
def file_open(file_open):
    file_min = os.listdir(f'{file_open}')
    file_min.sort()
    
    return file_min




# 코스피 코스닥(일봉) 업데이트
def update_day_stock_info(file_day, dir_day_open, dir_day_update_save):
    
    for file_name in tqdm(file_day):
        temp_df = pd.read_csv(f'{dir_day_open}{file_name}', index_col='Unnamed: 0', encoding='utf-8 sig')
        
        stock_code = file_name.split('_')[-2] # 종목 코드 분할
        
        start_day = str(temp_df.index[0])

        today = str(datetime.today().year) + str(datetime.today().month) + str(datetime.today().day)

        instStockChart.SetInputValue(0, 'A'+stock_code) # 종목명
        instStockChart.SetInputValue(1, ord('1')) # 1 : 기간으로 요청, 2: 개수로 요청
        instStockChart.SetInputValue(3, start_day) # 요청 시작일
        instStockChart.SetInputValue(2, today) # 요청 종료일
        instStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 16, 17,18, 19,20,21,22,23,24,25,26])
        instStockChart.SetInputValue(6, ord('D')) # 'D' : 일봉, 'm' : 분봉
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

        update_day_df = pd.concat([stock_info, temp_df])
        
        update_day_df.to_csv(f'{dir_day_update_save}{file_name}', encoding='utf-8 sig')

    return update_day_df



# 분봉 일봉 합치기
def save_min_day_concat_param(file_min_update, file_day_update, dir_min_update, dir_day_update, dir_concat_save):
    for min_df, day_df in zip(file_min_update, file_day_update):
        stock_min_df = pd.read_csv(f'{dir_min_update}{min_df}', index_col='Unnamed: 0')
        stock_day_df = pd.read_csv(f'{dir_day_update}{day_df}', index_col='Unnamed: 0')
        
        concat_list = []
        concat_list.append('A' + min_df.split('_')[-2])
        
        for v in tqdm(stock_min_df.index):
            input_list = ['전일대비','상장주식수','시가총액','외국인주문한도수량'
                    ,'외국인주문가능수량','외국인현보유수량','외국인현보유비율'
                    ,'수정주가일자','수정주가비율','기관순매수량','기관누적순매수량']
            
            stock_min_df.loc[v, input_list] = stock_day_df.loc[v, input_list].values
        for code in concat_list:        
            stock_min_df.to_csv('{0}concat_{1}_{2}.csv'.format(
                            dir_concat_save, search_by_code(code)[0][1:],search_by_code(code)[1]
                            ), encoding='utf-8-sig')           
            
            
# 라벨링 처리
def save_label_stock_info_param(file_concat, dir_concat_open, dir_label_save):
    
    for file_name in tqdm(files_concat):
        stock_info = pd.read_csv(f'{dir_concat_open}{file_name}', index_col=0)
        
        concat_list =  []
        concat_list.append('A' + file_name.split('_')[-2])

        # 데이터 프레임에서 날짜 인덱스 추출
        date = stock_info.index.unique()
        # label 컬럼 추가 후 0으로 초기화
        stock_info['label'] = 0
        # 업데이트에 사용할 데이터 프레임 생성
        update_stock_info = pd.DataFrame()

        # labeling
        for day in date:
            # 특정일의 Data 추출
            select_day = stock_info.loc[day].copy()
            select_day['label'] = 0
     
            # 특정일의 Row 만큼 반복
            for row in range(len(select_day)): 
                # 특정일의 현재 row 이후 최대 고가를 추출
                next_price = select_day[-row-1::-1]['고가'].max()
                # 추출한 최대 고가를 label 컬럼에 대입
                select_day.iloc[-row-1,-1] = next_price
                next_price = 0
            # 특정일 label이 추가된 DF를 업데이트할 DF에 concat
            update_stock_info = pd.concat([update_stock_info, select_day])       
        # 업데이트된 DF 저장
        for code in concat_list:
            update_stock_info.to_csv('{0}label_{1}_{2}.csv'.format(
                dir_label_save, search_by_code(code)[0][1:],search_by_code(code)[1]
                ), encoding='utf-8-sig')