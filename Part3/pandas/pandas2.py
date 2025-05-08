import pandas as pd

df = pd.read_csv(r'Part3\pandas\credit.csv')

# 나이와 사용금액
print(df[['나이','사용금액']].corr())

# 필터
# print(df[ df['나이'] > 50 ])
print(df.query("나이 > 50 and 기혼 == 'Married' "))

# list > dataframe
셔츠 = [15,20,25]
바지 = [150,160,170]

dic = {
    '셔츠': [15,20,25],
    '바지' : [150,160,170]
}

df2 = pd.DataFrame(dic)
print(df2)