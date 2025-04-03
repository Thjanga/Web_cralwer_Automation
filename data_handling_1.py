import requests
import json
import time

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/krw/eth?interval=1h')
# print(data.content)
dic = json.loads(data.content)

for i in range(200):
    day = dic['body']['candles'][i]['dt']  
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(day / 1000)))
    print(dic['body']['candles'][i]['close']) 


