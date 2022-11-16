# dataframe_contact.py

# 데이터프레임 관련
import numpy as np
import pandas as pd

# 시간 관련
import time
from tqdm import tqdm

# 파일, 텍스트 관련
import re
import os
import glob


# 파일 리스트 만들기
# 실제 파일 이름 공백 제거
# path: 파일 경로 (파일 이름 전)
# file_extension : 파일 확장자 (. 제외)
# delete_ste : 파일 이름 리스트에서 제외할 문자열
# file_list, file_names list, tuple로 반환
def file_list_make(path: str, file_extension: str, delete_str: str):
	file_names = []
	temp_path = glob.glob(path + '/*.' + file_extension)

	# 파일 이름 공백 제거
	for file_path in temp_path:
		if file_path.find(' '):
			path = file_path.replace(' ', '_')
			os.rename(file_path, path)
		else:
			pass

	file_list = temp_path

	for file in file_list:
		file_name = file.split('/')[-1].split('.')[0]
		if delete_str.find('_'):
			name = file_name.replace('_' + delete_str, '')
		else:
			name = name = file_name.replace(delete_str, '')
		file_names.append(name)

	print(file_list)
	print(file_names)

	return file_list, file_names


# 데이터 프레임 합치기
# file_list : 파일 리스트
# file_names : 파일 이름 리스트
# concat_df_name : 최종 반환할 데이터 프레임 이름
# axis : concat 방향, default 1
def dataframe_conact(file_list: list, file_names: list, concat_df_name: str, axis=1):
	temp_list = []

	for idx, file in enumerate(file_list):
		temp = pd.read_csv(file, index_col='날짜', encoding='utf-8')

		# 컬럼 이름 변경
		name = file_names[idx] + '_'
		temp.rename(columns=lambda x: name + x, inplace=True)

		# 데이터 프레임 합치기
		temp_list.append(temp)
		concat_df_name = pd.concat(temp_list, axis=axis, join='inner').reset_index()

	print('concat 완료!!!!')

	return concat_df_name


# 데이터프레임 저장하기
# df_name: 저장 할 이름
# save_path: 저장 경로
# file_extension: 파일 확장자 defualt : csv
def dataframe_save(df_name, save_path, file_extension='csv'):
	pd.to_csv(save_path + df_name + '.' + file_extension)
	return print('파일 저장됨!')


# 날짜 형식 숫자로만 바꾸기
def date_format_change(file_list):
	regx = '[가-힣]'

	for idx, file in enumerate(file_list):
		df = pd.read_csv(file)
		df['날짜'] = df['날짜'].apply(lambda x: re.sub(regx, '', x))
		df['날짜'] = df['날짜'].apply(lambda x: x.replace(' ', ''))
		df.sort_values(['날짜'], inplace=True)
		df.to_csv('/Users/hwanghyeonjun/Documents/GitHub/data/selenium/' + file_names[idx], index=False)


# 날짜 순서로 오름차순정렬
def dataframe_srot(file_list):
	file_names = []

	for path in tqdm(file_list):
		file_name = path.split('/')[-1]
		file_names.append(file_name)

	for idx, file in tqdm(enumerate(file_list)):
		df = pd.read_csv(file)
		df.sort_values(['날짜'], inplace=True)
		df['날짜'] = df['날짜'].apply(lambda x: x.replace(' ', ''))
		df.to_csv('/Users/hwanghyeonjun/Documents/GitHub/data/selenium/' + file_names[idx], index=False)
