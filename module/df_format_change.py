# df_format_change.py
import time

from tqdm import tqdm

# 데이터프레임 관련
import numpy as np
import pandas as pd

# 파일, 텍스트 관련
import re
import glob

from unicodedata import normalize


# 파일 리스트 만들기
# 실제 파일 이름 공백 제거
# path: 파일 경로 (파일 이름 전)
# file_extension : 파일 확장자 (. 제외)
# delete_str : 파일 이름 리스트에서 제외할 문자열 default: ''(빈문자열)
# file_list, file_names list, tuple로 반환
def file_name_list(path: str, file_extension: str) -> tuple:
	file_names = []

	file_list = glob.glob(path + '/*.' + file_extension)

	for file in file_list:
		try:
			file_name = file.split('/')[-1].split('.')[0]
			name = file_name.replace(' ', '').replace('_', '').replace('&', '')
			normalize_name = normalize('NFC', name)
			file_names.append(normalize_name)
		except:
			pass

	return file_list, file_names


# 데이터 프레임 합치기
# file_list : 파일 리스트
# file_names : 파일 이름 리스트
# concat_df_name : 최종 반환할 데이터 프레임 이름
# axis : concat 방향, default 1
def df_conact(file_list: list, file_names: list, concat_df_name: str, axis=1) -> pd.DataFrame:
	temp_list = []

	for idx, file in enumerate(file_list):
		temp = pd.read_csv(file, index_col='날짜', encoding='utf-8')

		# 컬럼 이름 변경
		name = file_names[idx] + '_'
		temp.rename(columns=lambda x: name + x, inplace=True)

		# 데이터 프레임 합치기
		temp_list.append(temp)
		concat_df_name = pd.concat(temp_list, axis=axis, join='inner').reset_index()

	return concat_df_name


# 데이터프레임 저장하기
# df_list: 데이터프레임 리스트
# df_name: 저장 할 이름
# save_path: 저장 경로
# file_extension: 파일 확장자 defualt : csv
def df_save(df_list: list, df_names: list, save_path: str, file_extension='csv') -> None:
	for idx, dataframe in enumerate(df_list):
		print(dataframe)
		try:
			dataframe.to_csv(save_path + '/' + df_names[idx] + '.' + file_extension)
		except:
			print('저장 오류')


# 날짜 형식 숫자로만 바꾸기
# 데이터 형식 바꾸기
# file_list : 파일 리스트
# file_name : 파일 이름 리스트
# 데이터프레임 리스트 반환
def data_format_change(file_list: list, file_names: list) -> list:
	df_list = []
	for idx, file in enumerate(tqdm(file_list)):
		try:
			date_regx = '\D?\s?'
			persent_regx = '\d+[%]$'

			prices = ['종가', '오픈', '고가', '저가']

			volumes = []

			load_df = pd.read_csv(file)
			df = load_df.astype(str)

			if str(list(load_df['날짜'].values)[0]) == '결과를 찾을 수 없습니다':
				file_list.pop(idx)
				file_names.pop(idx)
			else:
				pass

			df.rename(columns={'변동 %': '변동'}, inplace=True)

			df['날짜'] = df['날짜'].apply(lambda x: re.sub(date_regx, '', x))

			for price in prices:
				df[price] = df[price].apply(lambda x: x.replace(',', '')).astype('float')

			if '거래량' in list(df.columns):
				df['거래량'] = df['거래량'].apply(lambda x: x.replace(',', ''))

				for volume in df['거래량'].values:
					cash_unit = list(volume)[-1]

					if str(volume) == 'nan':
						n = str(volume).replace('nan', '0')
						volumes.append(float(n))
					elif cash_unit == 'K':
						k = volume.replace(cash_unit, '')
						k_result = round(float(k) * 1000)
						volumes.append(k_result)
					elif cash_unit == 'M':
						m = volume.replace(cash_unit, '')
						m_result = round(float(m) * 1000000)
						volumes.append(m_result)
					elif cash_unit == 'B':
						b = volume.replace(cash_unit, '')
						b_result = round(float(b) * 1000000000)
						volumes.append(b_result)

				df['거래량'] = volumes
			else:
				df.insert(5, '거래량', 0, allow_duplicates=False)

			df['변동'] = df['변동'].apply(lambda x: x.replace(',', ''))

			if not bool(re.match(persent_regx, list(df['변동'])[0])):
				df['변동'] = df['변동'].apply(lambda x: x.replace('%', '')).astype('float')

			df.sort_values(['날짜'], inplace=True)

			col_name = df.columns[1:]

			for col in col_name:
				df.rename(columns={col: file_names[idx] + '_' + col}, inplace=True)

			df_list.append(df)
		except:
			pass

	return df_list


# 날짜 형식 숫자로만 바꾸기
# 데이터 형식 출력용으로 바꾸기
# 데이터프레임 리스트 반환
def column_name_change(df_list: list) -> list:
	column_name_change_list = []
	eng_name = ['dates', 'closes', 'opens', 'highs', 'lows', 'volumes', 'changes']

	for df in df_list:
		col_name = df.columns
		for idx, col in enumerate(col_name):
			df.rename(columns={col: eng_name[idx]}, inplace=True)

		column_name_change_list.append(df)

	return column_name_change_list
