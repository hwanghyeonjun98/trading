import pandas as pd
import numpy as numpy
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql


import requests
from bs4 import BeautifulSoup

main_url = 'https://finance.naver.com'
sub_url = '/news/mainnews.naver'
url = main_url + sub_url

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('#contentarea_left > div.mainNewsList > ul > li > dl > dd > a')
    
else : 
    pass
    
newsname = []
titles = soup.select('dd.articleSubject')

for i in titles:
    titlele = i.get_text().replace('\n','')
    newsname.append(titlele)


soup = BeautifulSoup(html, 'html.parser')
list_ = []
for each in title:
    href = main_url + each['href']
    list_.append(href)


newsct= []
for newslist in list_:
    response = requests.get(newslist)
    

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        contents = soup.select_one('.articleCont')
        cnt = contents.get_text().replace('\n','')[:500]
        
    else : 
        print(response.status_code)
    newsct.append(cnt)    
    


data = {'Newsname':newsname,'Newslink':list_,'News':newsct}
df = pd.DataFrame(data)
df.head()

pymysql.install_as_MySQLdb()
conn= pymysql.connect(
    host="192.168.50.123"
    ,user="admin"
    ,password="big15"
    ,db= "web_data"
    ,charset='utf8'
)

cursor = conn.cursor()
args = df.values.tolist()

sql_update= f"""
INSERT INTO news_data
VALUES (%s,%s,%s)
ON DUPLICATE KEY UPDATE
    newsname= VALUES(newsname)
    ,newslink= VALUES(newslink)
    ,news = VALUES(news)
"""

cursor.executemany(sql_update, args)

conn.commit()
conn.close()



