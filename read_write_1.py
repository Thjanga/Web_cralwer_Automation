리스트 = ['삼성전자','카카오','네이버','신풍제약']

f = open('1.txt','w',encoding='UTF-8')
for i in 리스트:
    f.write(i)
    f.write("\n")
f.close()