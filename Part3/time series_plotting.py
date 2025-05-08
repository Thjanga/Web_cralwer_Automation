import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt 

df = yf.download('005930.KS', start='2024-05-07', end='2025-05-07')

close_price = df['Close']
mean5 = df['Close'].rolling(5).mean()
mean20 = df['Close'].rolling(20).mean()
plt.plot(close_price)
plt.plot(mean5)
plt.plot(mean20)
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.show()
