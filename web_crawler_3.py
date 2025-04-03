import requests
from bs4 import BeautifulSoup

종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']

def get_data(num):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={num}')
    soup = BeautifulSoup(data.content,'html.parser')
    # print(soup.find_all('strong',id="_nowVal")[0].text) # 현재가
    # print(soup.find_all('span',class_="tah")[5].text) # 거래량
    return soup.find_all('strong',id="_nowVal")[0].text

f = open("2.txt","w")
for i in 종목들:
    f.write(get_data(i))
    f.write('\n')
f.close