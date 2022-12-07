# file_remove.py

import os
import shutil

# csv파일 SQL로 업로드 후 파일 삭제
def file_remove(file_list: list) -> None:
	for file in file_list:
		os.remove(file)


# 파일 이동
def file_move(file_list: list, move_path: str) -> None:
	for file in file_list:
		shutil.move(file, move_path)