import pandas as pd

df = pd.read_csv(r'Part3\pandas\credit.csv')
# print(df)
# print(df['나이'].mean())
# print(df['나이'].mode())
# print(df['나이'].max())
# print(df['나이'].min())
# print(df['나이'].describe())

print(df.groupby('성별').mean())