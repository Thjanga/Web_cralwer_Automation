import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt 

# df = yf.download('005930.KS', start='2024-05-07', end='2025-05-07')

# # 선그래프
# plt.plot(df.index,df['Close'],color="crimson")
# plt.figure(figsize=(10,10))
# plt.xlabel('time')
# plt.ylabel('price')
# plt.legend(['S'])
# plt.show()

# # 막대차트
# plt.bar(df.index,df['Close'])
# plt.show()

# # 파이차트
# plt.pie([57,35,11],labels=['ramen','tuna','snack'])
# plt.show()

# # 히스토그램
# plt.hist([160,165,170,171,172,180])
# plt.show()

# # 분포도
# math = [5,8,23,5,67,34,34,23]
# eng = [23,6,3,1,5,45,54,34]
# plt.scatter(math, eng)
# plt.show()

# # 스택차트
# plt.stackplot(['A','B','C'], [10,20,30], [30,20,50], [10,20,30])
# plt.show() 

# Q1
# df = yf.download('AMZN',start='2020-01-01',end='2020-12-31')

# mean20 = df['Close'].rolling(20).mean()
# mean60 = df['Close'].rolling(60).mean()

# plt.plot(df.index,mean20)
# plt.plot(df.index,mean60)
# plt.plot(df.index,df['Close'])
# plt.show()

# Q2
# plt.plot([2018,2019,2020,2021], [50000,60000,75000,70000])
# plt.plot([2018,2019,2020,2021], [30000,40000,50000,35000])
# plt.xlabel('time')
# plt.ylabel('sales')
# plt.legend(['Samsung', 'Lg'])
# plt.show()
# plt.show()

# Q3
df = yf.download('BTC-USD',start='2020-01-01',end='2020-12-31')

df2 = df[df['Volume']>df['Volume'].mean()]

plt.plot(df2.index, df2['Close'])

plt.show()