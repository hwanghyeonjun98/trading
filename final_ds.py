from final_db_update import *
from final_investing_update import investing_update

# DB의 데이터를 업데이트
db_list_update(krx=r'D:\systrader-dev\trading\download\krx')    # 각자 컴퓨터의 맞게 변경   # 32bit

# investing 데이터 업데이트
investing_update(path=r'D:\systrader-dev\trading\download\investing')     # 각자 컴퓨터의 맞게 변경