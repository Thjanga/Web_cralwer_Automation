import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930') # 삼성전자
soup = BeautifulSoup(data.content,'html.parser')
print(soup.find_all('strong',id="_nowVal")[0].text) # 현재가
print(soup.find_all('span',class_="tah p11")[0].text) # 거래량

data = requests.get('https://finance.naver.com/item/main.naver?code=000660') # SK 하이닉스
soup = BeautifulSoup(data.content,'html.parser')
print(soup.find_all('strong',id="_nowVal")[0].text) # 현재가
print(soup.find_all('span',class_="tah p11")[0].text) # 거래량
