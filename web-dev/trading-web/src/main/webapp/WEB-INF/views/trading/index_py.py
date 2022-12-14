import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup
import urllib.request

url='https://finance.naver.com/sise/' #주소를 변수에 넣기

resp = urllib.request.urlopen(url) # url을 넣어 html형식으로 돌려받는다.


soup = BeautifulSoup(resp,'html.parser',from_encoding='euc-kr') 

sises = soup.find('ul',{'class' : 'lst_pop'}) # class가 lst_pop인 ul 태그를 찾는다.


sises_kor = sises.select('li') # sises에서 li 태그를 찾음

for sise in sises_kor: #반복
    title = sise.find('a').text  # a 태그를 text로 가져온다.
    result = sise.find('span').text # span 태그를 text로 가져온다.
    print(f'{title} \t {result}') # title과 result 출력



