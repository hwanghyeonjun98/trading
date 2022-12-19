# data_sql_load.py

from tqdm import tqdm

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
def df_sql_save(user: str, password: str, host: str, port: str, db: str, df_list: list, file_names: list, if_exists='replace') -> None:
	engine = create_engine(
		"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8".format(
			user=user, password=password, host=host, port=port, db=db
		)
		, encoding='utf8'
	)

	for idx, df in enumerate(tqdm(df_list)):
		df.to_sql(name=file_names[idx].lower(), con=engine, if_exists=if_exists, index=False, method='multi')


# 최신 데이터 SQL 저장
# 기본 데이터가 없으면 insert, 있으면 update
def sql_update(user: str, password: str, host: str, db: str, df_list: list, file_names: list) -> None:
	pymysql.install_as_MySQLdb()
	conn = pymysql.connect(
		host=host
		, user=user
		, password=password
		, db=db
		, charset='utf8'
	)

	cursor = conn.cursor()
	for idx, df in enumerate(tqdm(df_list)):
		table_name = file_names[idx]
		args = df.values.tolist()

		col1 = df.columns[0]
		col2 = df.columns[1]
		col3 = df.columns[2]
		col4 = df.columns[3]
		col5 = df.columns[4]
		col6 = df.columns[5]
		col7 = df.columns[6]

		sql_update = f"""
		INSERT INTO `{table_name}`
		VALUES (%s,%s,%s,%s,%s,%s,%s)
		ON DUPLICATE KEY UPDATE
			`{col1}` = VALUES(`{col1}`)
			,`{col2}` = VALUES(`{col2}`)
			,`{col3}` = VALUES(`{col3}`)
			,`{col4}` = VALUES(`{col4}`)
			,`{col5}` = VALUES(`{col5}`)
			,`{col6}` = VALUES(`{col6}`)
			,`{col7}` = VALUES(`{col7}`)
		"""
		cursor.executemany(sql_update, args)

	conn.commit()
	conn.close()
