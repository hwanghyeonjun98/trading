# sql_save.py

import numpy as np
import pandas as pd

# sql 관련
import pymysql
from sqlalchemy import create_engine


# 새 데이터 프레임 sql로 저장
# user : sql 사용자 이름
# password : sql 사용자의 비밀번호
# host : sql host(ip, 도메인)
# port : sql port
# db : database 이름
# df_list : data_format_change 반환값
# file_names : file_name_list 반환값
# if_exists : sql로 업로드 시 같은 이름의 테이블이 있으면
#             fail => 기존 내용이 있으면 적용 안함
#             replace => 기존 테이블을 삭제하고 새로 테이블 생성
#             append => 테이블이 존재하면 기본 테이블에 데이터 삽입
def df_sql_save(user: str, password: str, host: str, port: str, db: str, df_list: list, file_names: list, if_exists='append') -> None:
	engine = create_engine(
		"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8".format(
			user=user, password=password, host=host, port=port, db=db
		)
		, encoding='utf8'
	)

	for idx, df in enumerate(df_list):
		df.to_sql(name=file_names[idx], con=engine, if_exists=if_exists, index=False, method='multi')


# 최신 데이터 SQL 저장
# if_exists='append' 기존 테이블에 마지막 행에 추가 됨
def new_data_sql_save(user: str, password: str, host: str, port: str, db: str, df_list: list, file_names: list, if_exists='append') -> None:
	engine = create_engine(
		"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8".format(
			user=user, password=password, host=host, port=port, db=db
		)
		, encoding='utf8'
	)

	for idx, df in enumerate(df_list):
		try:
			last_df = df.iloc[-1:, :]
			last_df.to_sql(name=file_names[idx], con=engine, if_exists=if_exists, index=False)
		except:
			pass
