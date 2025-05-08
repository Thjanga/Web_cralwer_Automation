import pandas as pd

raw = pd.read_excel(r'Part3\pandas\product.xlsx',engine='openpyxl')

# raw['부가세포함'] = raw['판매가'] * 1.1

def f(a):
    return a * 1.1

raw['부가세포함'] = raw['판매가'].apply(f)

import re # 글자 판단 (정규식)

def f2(a):
    a = str(a)
    if re.search('Chair',a):
        return '의자'
    if re.search('Table',a):
        return '테이블'
    
raw['카테고리'] = raw['상품목록'].apply(f2)

print(raw)
