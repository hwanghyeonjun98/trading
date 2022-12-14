from module.selenium_crawling import selenium_driver_load, login, world_indices, world_rate_bonds_list, investing_crawling, investing_coins, investing_crawling_new
from module.df_format_change import file_name_list, data_format_change, column_name_change
from module.data_file_control import file_move
from module.data_sql_load import sql_update

import time

# investing 자료 업데이트 크롤링
def investing_update(path):
    driver = selenium_driver_load(
        './driver/chromedriver'
        , 'https://kr.investing.com/?ref=www'
        , path
    )
    start_date = '2020-01-01'
    login('widrn1010@naver.com', 'Aa10101010!', driver)
    # 주요 환율 리스트
    currencies_names = ['USD', 'JPY', 'EUR', 'CNY', 'HKD', 'GBP', 'CHF', 'CAD', 'AUD', 'NZD', 'SEK', 'DKK', 'NOK', 'SAR',
                        'KWD', 'BHD', 'AED', 'THB', 'SGD', 'IDR', 'INR', 'MYR', 'PKR', 'BDT', 'EGP', 'MXN', 'BND']
    # 암호화폐
    coins = [['bitcoin', 'btc-krw'], ['ethereum', 'eth-krw'], ['xrp', 'xrp-krw']]
    commodities = ['gold', 'crude-oil', 'silver', 'natural-gas', 'copper', 'us-wheat']
    indices = world_indices()
    # 채권
    rate_bonds_id = ['60', '1', '20', '54', '4', '5', '3', '49', '9', '40']
    rate_bonds = world_rate_bonds_list(rate_bonds_id)
    investing_crawling('currencies', currencies_names, start_date, driver, '-krw')
    time.sleep(10)
    investing_crawling('indices', indices, start_date, driver)
    time.sleep(20)
    investing_crawling('commodities', commodities, start_date, driver)
    time.sleep(5)
    investing_coins(coins, start_date, driver)
    time.sleep(8)
    investing_crawling_new('rates-bonds', rate_bonds, start_date, driver)
    driver.close()
    file_list, file_names = file_name_list(
        './download/investing/'
        , 'csv'
    )
    df_list = data_format_change(file_list, file_names)
    sql_update('admin', 'big15', '192.168.50.123', 'investing_data', df_list, file_names)
    web_data = column_name_change(df_list)
    sql_update('admin', 'big15', '192.168.50.123', 'web_data', web_data, file_names)
    file_move(file_list, f'./download/temp/', file_names)