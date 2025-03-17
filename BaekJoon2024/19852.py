a1 , b1 = map(int,input().split())
a2 , b2 = map(int,input().split())
a3 , b3 = map(int,input().split())

a1_digits = [int(a1) for a1 in str(a1)]
b1_digits = [int(b1) for b1 in str(b1)]
a2_digits = [int(a2) for a2 in str(a2)]
b2_digits = [int(b2) for b2 in str(b2)]
a3_digits = [int(a3) for a3 in str(a3)]
b3_digits = [int(b3) for b3 in str(b3)]




def find_friends(a,b):
    a1 = set(a)
    b1 = set(b)
    if a1 == b1:
        return True
    else:
        return False
    
def find_almost_friends(a,b):
    for i in range(len(a)-1):
        if not(i == 0 and a[i] == 1):
            a[i] -= 1
            a[i+1] += 1
            if find_friends(a,b):
                return True
            a[i] += 1
            a[i+1] -= 1
        
        a[i] += 1
        a[i+1] -= 1
        
        if find_friends(a,b):
            return True
        
        a[i] -= 1
        a[i+1] += 1
        
        
    
    
        