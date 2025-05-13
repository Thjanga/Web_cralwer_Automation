import numpy as np
import statsmodels.api as sm
import pandas as pd

# 키 = np.array([170,180,160,165,158,176,182,172]).reshape((-1,1))
# 몸무게 = [75,81,59,70,55,78,84,72]

# model = sm.OLS(몸무게, 키).fit()
# print(model.summary())

df = pd.read_csv(r'Part3\california_housing.csv')

# 집값 = year * ? + rooms * ? + bedrooms * ?
model = sm.OLS(df['price'],df[['year','rooms','bedrooms']]).fit()
print(model.summary())

a = model.predict([20,1000,200])
print(a)