from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_table(r'Part3\income.txt')
df = df.dropna()

# plt.scatter(df['age'],df['income'])
# plt.show()

# y = ax^2 + bx + c

def 함수(x,a,b,c):
    return a*x**2 + b*x + c
opt, cov = curve_fit(함수,df['age'],df['income'])

# 행렬 쓸 때
x = np.array([1,2,3,4,5,6])

print(opt)
a,b,c = opt
plt.scatter(df['age'],df['income'])
plt.plot(x,함수(x,a,b,c))
plt.show()
