from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm

df = pd.read_table(r'Part3\income.txt')
df = df.dropna()

# x, x^2, 1
# x = np.column_stack([df['age'],df['age']**2, np.ones(79)])
x = np.column_stack([df['age'],df['age']**2])
model = sm.OLS(df['income'],x).fit()
print(model.summary())

# overfitting 현상
# 커브가 너무 많아지면 과적합 현상이 일어남 > 응용력이 없는 모델

