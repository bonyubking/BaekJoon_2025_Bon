T = int(input())
x_T = [0,0,0,0]
y_T = [0,0,0,0]

def findlen(a,b,c,d):
    key = ((a-c)**2+(b-d)**2)**(1/2)
    return key


for i in range(T):
    for i in range(4):
        x_T[i], y_T[i] = map(int,input().split())
    
    
    Tlist = [findlen(x_T[0],y_T[0],x_T[1],y_T[1]), findlen(x_T[0],y_T[0],x_T[2],y_T[2]),findlen(x_T[0],y_T[0],x_T[3],y_T[3]),findlen(x_T[1],y_T[1],x_T[2],y_T[2]),findlen(x_T[1],y_T[1],x_T[3],y_T[3]),findlen(x_T[2],y_T[2],x_T[3],y_T[3])]
    
    
    Tlist.sort()
    
    if Tlist[0] == Tlist[1] == Tlist[2] == Tlist[3] and Tlist[4] == Tlist[5]:
        print('1')
        
    else:
        print('0')


