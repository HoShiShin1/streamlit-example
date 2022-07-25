import requests

import json

 

str = input("分析されるユーザIDを入力さ")

url1 = 'https://api.booklog.jp/v2/json/'

url2 = '?count=24'

url = url1 + str + url2

 

api_res=requests.get(url)

json_res=json.loads(api_res.text)

 

 

data = api_res.json()

books = data['books']

from pandas import DataFrame

 

if len(books) < 20:

 print("データが不足、アプリを終了する!")

else:

 

 

 df = DataFrame(books)

 

 import datetime

 

 def format_date(date_str):

     date_format = '%Y年%m月%d日'

     # 2021-07-22 00:00:00 のように変換

     date_dt = datetime.datetime.strptime(date_str, date_format)

 

     year=date_dt.year

 

     # 0埋めで2文字

     month=f'{date_dt.month:02}'

 

     date=f'{year}{month}'

     return date

 

 from bs4 import BeautifulSoup

 import requests

 

 for book in books:

   url = book['url']

   html = requests.get(url)

   soup = BeautifulSoup(html.content, "html.parser")

   register_date=soup.find(class_='read-day-status-area').find('span').text

   print(register_date)
 book['register_date'] = register_date

book['register_mon'] = format_date(register_date)

df2 = DataFrame(books)

df2

 

g = df2.groupby('register_mon').count()
g
