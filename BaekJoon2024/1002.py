# 0 0
# 0 7
# 3 4

# 1 1
# 1 1
# 1 5


# r1 + r2가 x 에서 y 거리일떄 ans = 1

# x 랑 y가 같은데 r1 != r2 일때 ans = 0

# x y같고 r1 = r2일때 ==> 무한대

# else 2
import math


case_Num = int(input())


def distance(a,b,c,d):
    ans = ((a-c)**2+(b-d)**2)**(1/2)
    return ans


for i in range(case_Num):
    x1, y1, r1, x2, y2, r2 = map(int,(input().split()))
    
    if (r1 + r2) == distance(x1,y1,x2,y2) or abs(r1-r2) == distance(x1,y1,x2,y2):
        print('1')
        
    elif distance(x1,y1,x2,y2) == 0 and r1 == r2:
        print('-1')
        
    elif abs(r1-r2) < distance(x1,y1,x2,y2) < (r1+r2):
        print('2')
        
    else:
        print('0')    
