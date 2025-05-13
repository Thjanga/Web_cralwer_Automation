import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 리스트를 2차원으로 만듬
키 = np.array([170,180,160,165,158,176,182,172]).reshape(-1,1)
몸무게 = np.array([75,81,59,70,55,78,84,72])

plt.scatter(키,몸무게)
plt.show()

#OLS 오차 최소화
# y = ax + b
model = LinearRegression().fit(키,몸무게)
print(model.score(키,몸무게)) # 1과 가까울수록 밀접한 관계
print(model.intercept_) # b값
print(model.coef_) # a값
a = model.predict([[170],[180]])
print(a)

plt.scatter(키,몸무게)
plt.plot(키,model.predict(키))
plt.show()


