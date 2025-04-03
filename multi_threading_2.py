import requests
import json
import time

urls = [
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000",
    "https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000",
]

def craw(url):
    data = requests.get(url)
    dic = json.loads(data.content)
    return dic['data'][0]['Close']

# for i in urls:
#     print(craw(i))

# lists = [2,3,4,5,6]
# def add(x):
#     return x+1

# result = map(add, lists)
# print(list(result))

from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4)
result = pool.map(craw,urls)
pool.close()
pool.join()

print(result)