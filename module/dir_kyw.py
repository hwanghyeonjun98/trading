from module.def_mg import file_open

dir_min_open        = '../data/data_보통주/'          # 분봉 데이터 불러오기
dir_day_open        = '../data/day_보통주/'          # 일봉 데이터 불러오기
dir_min_update_open = '../data/update/20221116/분봉'   # 분봉 업데이트 저장
dir_day_update_open = '../data/update/20221116/일봉'   # 일봉 업데이트 저장

dir_min_update_save  = '../data_min_update/' # 분봉 업데이트 저장
dir_day_update_save  = '../data_day_update/' # 일봉 업데이트 저장


file_min        = file_open(dir_min_open )          # 분봉 데이터 리스트
file_day        = file_open(dir_day_open)           # 일봉 데이터 리스트
file_min_update = file_open(dir_min_update_open)    # 분봉 업데이트 리스트
file_day_update = file_open(dir_day_update_open)    # 일봉 업데이트 리스트