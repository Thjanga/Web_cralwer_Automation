import pandas as pd

df = pd.read_csv(r'Part3\pandas\credit.csv')

print(df.select_dtypes(include='number').groupby(df['소득']).mean())
