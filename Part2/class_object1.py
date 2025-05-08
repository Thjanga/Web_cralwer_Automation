# nunu = {
#   'q' : 'eat',
#   'w' : 'snowball'
# }
# garen = {
#   'q' : 'strike',
#   'w' : 'courage'
# }

# 오브젝트 한줄컷
class Hero:
    # q = 'eat'
    # w = 'snowball'
    
    def __init__(self): # 초기값
        self.q = 'eat'
        self.w = 'snowball'

nunu = Hero()
garen = Hero()
print(nunu.q)
print(garen.q)