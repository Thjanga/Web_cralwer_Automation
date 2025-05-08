import pandas as pd

df = pd.read_csv(r'Part3\pandas\credit.csv')

df2 = df.query("성별 == 'M' and 기혼 == 'Married'")['사용금액'].mean()

df3 = df.query("성별 == 'M' and 기혼 == 'Single'")['사용금액'].mean()

if df2>df3:
    print("Yes")
else:
    print("No")



