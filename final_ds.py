from final_db_update import *
from final_target import *
from investing_update import investing_update

# DB의 데이터를 업데이트
db_list_update(krx=r'D:\systrader-dev\trading\download\krx')    # 각자 컴퓨터의 맞게 변경   # 32bit

# investing 데이터 업데이트
investing_update(path=r'C:\big15\project-dev\trading\download')     # 각자 컴퓨터의 맞게 변경

# 예측할 종목 설정
kospi_list, kosdaq_list, investing_df = get_target(path=r'D:\systrader-dev\trading\download\target')

# if __name__ == "__main__":
#     traiding_start()

# realtime 추가