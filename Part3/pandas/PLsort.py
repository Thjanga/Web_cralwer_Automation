import pandas as pd

pf = pd.read_csv('Part3\pandas\PL.csv')
sorted = pf.sort_values(by='합산점수',ascending=False)
print(sorted)
