L = int(input())
Numlist = list(map(int,input().split()))
N = int(input())

def sorting():
    count = 0
    keynum = L
    while count != L:
        for i in range(keynum-1):
            if Numlist[i] > Numlist[i+1]:
                Num = Numlist[i]
                Numlist[i] = Numlist[i+1]
                Numlist[i+1] = Num
        
        count += 1
        keynum -= 1
   

def findanswer(keylist):    
    keylist.append(N)
    for i in range(0, L):
        if keylist[L-i] < keylist[L-i-1]:
            Num1 = keylist[L-i-1]
            keylist[L-i-1] = keylist[L-i]
            keylist[L-i] = Num1
            
    keylist.insert(0, 0)     
    keynum1 = keylist.index(N)
    ans = (N - keylist[keynum1-1])*(keylist[keynum1+1]- N) - 1
    
    if keylist[keynum1] == keylist[keynum1-1] or keylist[keynum1] == keylist[keynum1+1]:
        ans = 0
    
    return ans
    


sorting()
ans1 = findanswer(Numlist)


print(ans1)