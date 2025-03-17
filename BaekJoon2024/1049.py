A = list(map(int, input().split()))
N = A[1]
B = []
for i in range(0,N):
    B.append(list(map(int, input().split())))
    
setMin = min(r[0] for r in B) 
aloneMin = min(r[1] for r in B)
   
mok = A[0]//6
na = A[0]%6

Smin = min(aloneMin*na, setMin)

S = (setMin*mok + Smin)
S1 = (aloneMin*(A[0]))

ans = min(S,S1)

print(ans)

 
 