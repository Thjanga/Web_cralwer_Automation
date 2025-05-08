import requests
from bs4 import BeautifulSoup
import urllib.parse

def data_name(name):
    name = urllib.parse.quote(name)
    data = requests.get(f'https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query={name}&start=1&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_hty.top&nso=&prank=37&ngn_country=KR&lgl_rcode=&fgn_region=&fgn_city=&lgl_lat=&lgl_long=&enlu_query=IggCAJ2DULh%2FAAAA0tBxSPfYuIyKsj5Lnp1CZ0BzNzRSJb61imDjvZVJ9M3Z00S7m6hQ%2B%2FpUi7145a%2B611ML8b5aydy1Uk6nMXU0P1V0VznH36Ye7tY2fPC0XN7D7q22YEL9ME7IzplfHlOCRXTEFMhwsci%2BUaqVVgBxz3eBKxfiKU%2FOLNaqK0iAvip5VhblMdjyldnpH4SNq8G1uyv16GIaWHB1Hk4WpTLvZLFpn6%2FHsRJhe9V0xi7chAmjqPLeN7U7NjM8kZJQBCbrc75BLMOZi4xloqojcXXAi60GmGEv%2BvBL%2F3sQA6xXoZfL6xU4ycEjsNWsXJ%2FVfyVDwWzYtxrfAJ6odQNYLetBikl5fNx70vIyA0sqXGONLOw9eSior5ExWkPocBOsPlkrWwm2arKzGy2sMhhZaY1%2F502X8mb4LwhjeEfpTFOVwaQ08%2FuP9nNPZAqYz6NRzwRnVv%2BSSgzc%2FGxi1Efs5qdlbFgKMAX8AHO7iBPHwgw0zJdKqs4JhGARWCpk6ATXvqPn%2FgPsEDTycP1kGyWbazb7I8ChisuTnYcSnMm5mBMWOL42j7QodxVUTsd1ZHdwcrsSE9pZp%2B0u2vAkEDwtEqbijA%3D%3D&enqx_theme=IggCAHWCULhtAAAAh%2FDtntZaiMLGh3DOFtIyq%2B4EtXeapXTeRQEGir3RH5sIZYC78pRuLlbZcov6Ch0FtVs3mWV39sIRj%2BUQiRKQo684SoIzEONeXCE29%2B%2FwPif4HTqhPyA6b%2ByMB3R44L6h&abt=%5B%7B%22eid%22%3A%22PWC-AD-TAG%22%2C%22value%22%3A%7B%22bucket%22%3A%220%22%2C%22for%22%3A%22impression-neo%22%2C%22is_control%22%3Atrue%7D%7D%5D')
    soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
    글리스트 = soup.select("a.title_link")
    print(글리스트[0].text)
    print(글리스트[1].text)
    print(글리스트[2].text)
    print(글리스트[3].text)
    print(글리스트[4].text)

data_name('맛집')
data_name('사과')