Testcase = int(input())

def decide_inout(x1,y1,x2,y2,r):
    if (x1-x2)**2+(y1-y2)**2 < r**2:
        return 1
    else:
        return 2
    

for i in range(Testcase):
    x1,y1,x2,y2 = map(int,input().split())
    Number = int(input())
    cnt = 0
    for j in range(Number):
        x,y,r = map(int,input().split())

        case_1 = decide_inout(x1,y1,x,y,r) 
        case_2 = decide_inout(x2,y2,x,y,r)
        
        if case_1 == 1 and case_2 == 2:
            cnt += 1
            
        elif case_2 == 1 and case_1 == 2:
            cnt += 1
    
    
    print(cnt)

        
        
        

