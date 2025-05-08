# 오브젝트 한줄컷
class Hero:
    # q = 'eat'
    # w = 'snowball'
    
    def __init__(self,name1,name2): # 초기값
        self.q = name1
        self.w = name2
    
    def hello(self):
        print('Hello')

nunu = Hero('eat','snowball')
garen = Hero('strike','courage')
print(nunu.q)
print(garen.q)
nunu.hello()
garen.hello()