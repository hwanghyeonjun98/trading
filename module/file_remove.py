# file_remove.py

import os

# csv파일 SQL로 업로드 후 파일 삭제
def file_remove(file_list: list) -> None:
	for file in file_list:
		os.remove(file)
