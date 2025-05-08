import re
import pandas as pd

raw = pd.read_excel('Part3\pandas\product.xlsx',engine='openpyxl')

# a = re.search
# a = re.findall # 일치하는 글자 리스트로 반환

# [a-z], [A-Z], [] = or, [^] = not
# \d = 한자리 숫자 \d\d = 두자리 숫자 \d{2} = 두자리 숫자, \D = 숫자가 아닌 것, \s = 스페이스바, \S = 스페이스바 아닌 것(모든 문자)
# a+ = 반복
# re.IGNORECASE 대소문자 구분 x

re.sub('\-','.','2025-05-06')
re.sub('\d','','Abcde$f^g3545')

# Q1
결과 = re.findall('\S+@\S+\.\S+', 'abc@example.com')
print(결과)

# Q2
def 함수(a):
    a = str(a)
    if re.search('Mirror|Sofa',a):
        return '가구'

raw['카테고리'] = raw['상품목록'].apply(함수) 

# Q3
def 함수(a):
    a = str(a)
    if re.search('\d',a):
        return '에러'
    else:
        return a

raw['상품목록'] = raw['상품목록'].apply(함수) 