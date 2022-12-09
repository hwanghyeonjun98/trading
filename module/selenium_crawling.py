# selenium_crawling.py

import time
from tqdm import tqdm
from datetime import datetime
from datetime import timedelta

# 셀리움 import
from selenium import webdriver
from selenium.webdriver.common.by import By

# bs4 / 404 해결
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import urllib.request


# 셀리움 웹 드라이버 불러와서 실행
# 크롬 기준
def selenium_driver_load(driver_path: str, url: str, file_save_path: str) -> webdriver:
	print("크롤링 실행 중")
	options = webdriver.ChromeOptions()

	# 크롬 파일 저장 시 경로 설정
	options.add_experimental_option(
		"prefs", {
			"download.default_directory": file_save_path,
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing.enabled": True
		}
	)

	# 크롬창 안열고 크롤링 설정
	# options.add_argument('headless')
	# options.add_argument('window-size=1920x1080')
	# options.add_argument("disable-gpu")

	# user agent 설정
	user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
	options.add_argument('user-agent=' + user_agent)

	driver = webdriver.Chrome(driver_path, options=options)

	driver.get(url)

	login_modal = driver.find_element(By.XPATH, '//*[@id="PromoteSignUpPopUp"]')
	driver.implicitly_wait(100)
	if login_modal.is_displayed():
		driver.find_element(By.CSS_SELECTOR, '#PromoteSignUpPopUp > div.right > i').click()

	print("크롤링 실행")
	return driver


def login(email: str, password: str, driver) -> None:
	print('로그인 중')
	header_login_btn = '//*[@id="userAccount"]/div/a[1]'
	email_input = '//*[@id="loginFormUser_email"]'
	pw_input = '//*[@id="loginForm_password"]'
	login_btn = '//*[@id="signup"]/a'

	driver.implicitly_wait(100)
	driver.find_element(By.XPATH, header_login_btn).click()
	time.sleep(1)
	driver.find_element(By.XPATH, email_input).clear()
	driver.find_element(By.XPATH, pw_input).clear()
	driver.implicitly_wait(1)
	driver.find_element(By.XPATH, email_input).send_keys(email)
	driver.find_element(By.XPATH, pw_input).send_keys(password)
	time.sleep(1)
	driver.find_element(By.XPATH, login_btn).click()

	print('로그인')


# 현재 날짜
def now_date() -> str:
	now = datetime.now()
	datetime_ = now.strftime('%Y-%m-%d')
	days = datetime_

	return days


# 현재 날짜 - 일수
def day_calc(num: int) -> str:
	day = datetime.now() - timedelta(days=num)
	datetime_ = day.strftime('%Y-%m-%d')
	days = datetime_

	return days


# 인베스팅 과거 버전 페이지 크롤링
# 과거 버전, 새 버전 파라미터 동일
# middel_url : 서브 시작 URL
# names : 세부 URL
# start_date : 시작 날짜
# driver : selenium_driver_load 반환값
def investing_crawling(middel_url: str, names: list, start_date: str, driver: webdriver, suffix='', new_data='') -> None:
	print(middel_url + '크롤링 시작')
	start_date = start_date
	calender_btn = '.DatePickerWrapper_icon-wrap__cwTu_'
	start_year_input = '.NativeDateInput_root__wbgyP > input'
	apply_btn = 'HistoryDatePicker_apply-button__fPr_G'
	csv_download_btn = '.download-data_download-data__jxNYT > a'

	suffix_ = suffix

	# 셀리움 실행 코드
	for name in tqdm(names):
		name_ = name.lower()
		try:
			url = f'https://kr.investing.com/{middel_url}/{name_}{suffix_}-historical-data'

			driver.get(url)
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
			req = urllib.request.Request(url, headers=headers)
			urlopen(req)
			time.sleep(5)

			driver.execute_script('window.scrollTo(0, 320)')
			if new_data:
				driver.find_element(By.CSS_SELECTOR, calender_btn).click()
				driver.implicitly_wait(5)
				driver.find_element(By.CSS_SELECTOR, start_year_input).clear()
				driver.find_element(By.CSS_SELECTOR, start_year_input).send_keys(start_date)
				driver.implicitly_wait(5)
				driver.find_element(By.CLASS_NAME, apply_btn).click()
			else:
				pass
			time.sleep(6)
			driver.find_element(By.CSS_SELECTOR, csv_download_btn).click()
			driver.implicitly_wait(30)
		except HTTPError as e:
			driver.save_screenshot('./image.png')
			pass


# 인베스팅 새 버전 페이지 크롤링
def investing_crawling_new(middel_url: str, names: list, start_date: str, driver: webdriver, new_data='', suffix='') -> None:
	print(middel_url + '크롤링 시작')
	start_date = start_date
	calender_new_btn = '#flatDatePickerCanvasHol #datePickerIconWrap'
	start_year_new_input = '#startDate'
	apply_new_btn = '#applyBtn'
	csv_download_new_btn = '#column-content > div.float_lang_base_2.downloadDataWrap > div > a'

	modal = '.allow-notifications-popup'
	modal_close = '/html/body/div[6]/div/button'

	suffix_ = suffix

	# 셀리움 실행 코드
	for idx, name in enumerate(tqdm(names)):
		name_ = name.lower()
		try:
			url = f'https://kr.investing.com/{middel_url}/{name_}{suffix_}-historical-data'

			driver.get(url)
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
			req = urllib.request.Request(url, headers=headers)
			urlopen(req)
			time.sleep(5)

			try:
				allow_modal = driver.find_element(By.CSS_SELECTOR, modal)
				if allow_modal.is_displayed():
					driver.find_element(By.XPATH, modal_close).click()
			except:
				pass

			driver.execute_script('window.scrollTo(0, 320)')
			if new_data:
				driver.find_element(By.CSS_SELECTOR, calender_new_btn).click()
				driver.find_element(By.CSS_SELECTOR, start_year_new_input).clear()
				driver.implicitly_wait(1)
				driver.find_element(By.CSS_SELECTOR, start_year_new_input).send_keys(start_date)
				driver.implicitly_wait(5)
				driver.find_element(By.CSS_SELECTOR, apply_new_btn).click()
			else:
				pass
			time.sleep(10)
			driver.find_element(By.CSS_SELECTOR, csv_download_new_btn).click()
			driver.implicitly_wait(30)
		except HTTPError as e:
			driver.save_screenshot('./image.png')
			pass


# 암호화폐 크롤링
# 주소가 쳬계가 달라 따로 만듦
# coins : 2차원 배열
# start_date : 시작 날짜
# driver : selenium_driver_load 반환값
def investing_coins(coins: list, start_date: str, driver: webdriver, new_data='') -> None:
	print(str(coins) + '크롤링 시작')
	start_date = start_date
	calender_btn = '.DatePickerWrapper_icon-wrap__cwTu_'
	start_year_input = '.NativeDateInput_root__wbgyP > input'
	apply_btn = 'HistoryDatePicker_apply-button__fPr_G'
	csv_download_btn = '.download-data_download-data__jxNYT > a'
	for coin in tqdm(coins):
		try:
			url = f'https://kr.investing.com/crypto/{coin[0]}/{coin[1]}-historical-data'

			driver.get(url)

			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
			req = urllib.request.Request(url, headers=headers)
			urlopen(req)
			time.sleep(5)
			if new_data:
				driver.find_element(By.CSS_SELECTOR, calender_btn).click()
				driver.find_element(By.CSS_SELECTOR, start_year_input).clear()
				driver.implicitly_wait(1)
				driver.find_element(By.CSS_SELECTOR, start_year_input).send_keys(start_date)
				driver.implicitly_wait(5)
				driver.find_element(By.CLASS_NAME, apply_btn).click()
			else:
				pass
			time.sleep(6)
			driver.find_element(By.CSS_SELECTOR, csv_download_btn).click()
			driver.implicitly_wait(30)
		except HTTPError as e:
			driver.save_screenshot('./image.png')
			pass


# 세계 지수 리스트 가져오기
def world_indices() -> list:
	url = 'https://kr.investing.com/indices/major-indices'

	try:
		headers = {'User-Agent': 'Chrome/107.0.5304.87'}
		req = urllib.request.Request(url, headers=headers)
		html = urlopen(req)
	except HTTPError as e:
		err = e.read()
		code = e.getcode()
		print(err, code)

	soup = BeautifulSoup(html, 'html.parser')

	stock_link = soup.select(
		'td.datatable_cell__0y0eu.datatable_cell--name__5g25Q.table-browser_col-name__qzN_9 > div > a'
	)

	indices = []
	for each in stock_link:
		href = each['href']
		indice = href.split('/')[-1]
		indices.append(indice)

	return indices


def world_rate_bonds_list(rate_bonds_id: list) -> list:
	url = 'https://kr.investing.com/rates-bonds/world-government-bonds'

	try:
		headers = {'User-Agent': 'Chrome/107.0.5304.87'}
		req = urllib.request.Request(url, headers=headers)
		html = urlopen(req)
	except HTTPError as e:
		err = e.read()
		code = e.getcode()
		print(err, code)

	soup = BeautifulSoup(html, 'html.parser')

	rate_bonds_link = []
	for id_ in rate_bonds_id:
		rate_bond = soup.select(f'#rates_bonds_table_{id_} td.bold.left.noWrap.elp.plusIconTd > a')
		time.sleep(0.5)
		rate_bonds_link.extend(rate_bond)

	rate_bonds = []
	for each in rate_bonds_link:
		href = each['href']
		rate_bond = href.split('/')[-1]

		if rate_bond == 'russia-overnight-rate':
			pass
		elif rate_bond == 'russia-1-week-bond-yield':
			pass
		elif rate_bond == 'russia-2-week-bond-yield':
			pass
		elif rate_bond == 'russia-1-month-bond-yield':
			pass
		elif rate_bond == 'russia-2-month-bond-yield':
			pass
		elif rate_bond == 'russia-3-month-bond-yield':
			pass
		elif rate_bond == 'russia-6-month-bond-yield':
			pass
		elif rate_bond == 'turkey-1-year-bond-yield':
			pass
		else:
			rate_bonds.append(rate_bond)

	return rate_bonds
