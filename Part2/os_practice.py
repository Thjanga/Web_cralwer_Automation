# 파일 조작 모듈
import os

files = os.listdir(r'C:\Users\kspqi\Desktop\애플코딩 웹 크롤러, 업무자동화\Part2\test')

print(files)

# os.path.join('경로', '경로2')
# os.getcwd() # 경로 확인

# for i in os.listdir('C:/Users/kspqi/Desktop/애플코딩 웹 크롤러, 업무자동화/Part2/test'):
#     os.rename(f'C:/Users/kspqi/Desktop/애플코딩 웹 크롤러, 업무자동화/Part2/test/{i}',f'C:/Users/kspqi/Desktop/애플코딩 웹 크롤러, 업무자동화/Part2/test/a{i}')

# import shutil

# for i in os.listdir('C:/Users/kspqi/Desktop/애플코딩 웹 크롤러, 업무자동화/Part2/test'):
#     shutil.copy(f'C:/Users/kspqi/Desktop/애플코딩 웹 크롤러, 업무자동화/Part2/test/{i}',f'C:/Users/kspqi/Desktop/애플코딩 웹 크롤러, 업무자동화/Part2/test2/{i}')
