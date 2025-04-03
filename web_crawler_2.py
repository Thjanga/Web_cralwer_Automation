import requests
from bs4 import BeautifulSoup

def get_data(num):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={num}')
    soup = BeautifulSoup(data.content,'html.parser')
    print(soup.find_all('strong',id="_nowVal")[0].text) # 현재가
    print(soup.find_all('span',class_="tah")[5].text) # 거래량

get_data('005930')