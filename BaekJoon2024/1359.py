inputlist = list(map(int, input().split()))


N = inputlist[0]
M = inputlist[1]
K = inputlist[2]

def Combination(a, b):
    count = 1
    for i in range(0,b):
        count = (a-i)/(i+1) * count
    return int(count)    
        
        
def Findanswer(N1, M1, K1):
    Ans = 0
    for i in range(K1, M1+1):
        Ans = Ans + Combination(M1,i)*Combination((N1-M1),(M1-i))/Combination(N1,M1)
    
    return Ans    

Spot = Findanswer(N,M,K)
print(Spot)
        
    