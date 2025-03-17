a1 , b1 = map(int,input().split())
a2 , b2 = map(int,input().split())
a3 , b3 = map(int,input().split())

a1_digits = [int(a1) for a1 in str(a1)]
b1_digits = [int(b1) for b1 in str(b1)]
a2_digits = [int(a2) for a2 in str(a2)]
b2_digits = [int(b2) for b2 in str(b2)]
a3_digits = [int(a3) for a3 in str(a3)]
b3_digits = [int(b3) for b3 in str(b3)]


def findanswer(a, b):
    friendscount = 0
    almostcount = 0

    for i in range(1, len(a)-1):
        if a[i] in b:
            friendscount +=1
        else:
            if a[i]+1 in b and a[i+1]-1 in b:
                a[i] += 1
                a[i+1] -= 1
                almostcount += 1
            
            elif a[i]-1 in b and a[i+1]+1 in b:
                a[i] -= 1
                a[i+1] += 1
                almostcount += 1               
            elif a[i]+1 in b and a[i-1]-1 in b:
                a[i] += 1
                a[i-1] -= 1
                almostcount += 1
            
            elif a[i]-1 in b and a[i-1]+1 in b:
                a[i] -= 1
                a[i-1] += 1
                almostcount += 1                      
    if a[0] in b:
        friendscount += 1
    if a[len(a)-1] in b:
        friendscount += 1
                
    if friendscount == len(a):  
        return 0
    elif a[0] != 0 and friendscount == len(a)-1 and almostcount == 1:
        return 1
    elif a[0] != 0 and friendscount == len(a)-2 and almostcount == 1:
        return 1
    else:
        return 3
            

if findanswer(a1_digits,b1_digits) == findanswer(b1_digits,a1_digits) == 0:
    print('friends')
    
elif findanswer(a1_digits,b1_digits) == findanswer(b1_digits,a1_digits) == 3:
    print('nothing')
    
else:
    print('almost friends')
    
if findanswer(a2_digits,b2_digits) == findanswer(b2_digits,a2_digits) == 0:
    print('friends')
    
elif findanswer(a2_digits,b2_digits) == findanswer(b2_digits,a2_digits) == 3:
    print('nothing')
    
else:
    print('almost friends')
    
print(findanswer(a2_digits,b2_digits))
print(findanswer(b2_digits,a2_digits))

if findanswer(a3_digits,b3_digits) == findanswer(b3_digits,a3_digits) == 0:
    print('friends')
    
elif findanswer(a3_digits,b3_digits) == findanswer(b3_digits,a3_digits) == 3:
    print('nothing')
    
else:
    print('almost friends')


            

        
    
    
