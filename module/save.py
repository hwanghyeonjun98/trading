# 전체 일자 분봉 종목 데이터 가져와서 csv 파일로 저장
def save_stock_info_auto(stock_code, end_day, type):
    
    day_format = '%Y%m%d'
    minus_day = timedelta(days=1)
    
    stock_df = get_stock_info(stock_code, end_day, end_day, type) # 첫번째 DF 생성 => pre_day '20221028' end_day '20221103'
    
    stock_name = search_by_code(stock_code)

    for day in range(740): # range 범위 수정하지 말 것
        transfer_pre_day = datetime.strptime(end_day, day_format) # '20221028' '20221023'
        pre_day = datetime.strftime(transfer_pre_day - minus_day, day_format) # '20221023' '20221018'

        info_second = get_stock_info(stock_code, pre_day, pre_day, type) # '20221023' '20221027'

        time.sleep(0.15)
        end_day = pre_day
        print(pre_day)

        stock_df = pd.concat([stock_df, info_second], axis=0)
        info_second = pd.DataFrame()
        print(stock_df.shape)
        print(stock_name, 'Count : {0}, 남은 요청 횟수 :{1}'.format(day, instCpCybos.GetLimitRemainCount(1)))
        
        if  instCpCybos.GetLimitRemainCount(1) < 5:
            time.sleep(10)
    
    stock_df.to_csv('../data/{0}_{1}.csv'.format(stock_name[0][1:],stock_name[1]), encoding='utf-8-sig')

    return stock_df


# 분봉 일봉 합친 것 저장
def save_min_day_concat(concat_list):
        for c, code in tqdm(enumerate(concat_list)):
                globals()[f'data_m{c}'].to_csv('../data_concat/concat_{0}_{1}.csv'.format(
                                search_by_code(code)[0],search_by_code(code)[1]
                        ), encoding='utf-8-sig')