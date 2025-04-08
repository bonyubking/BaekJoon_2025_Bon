N = int(input())
lst = []

for i in range(1, N):
    k = i
    ans = i
    for j in range(1,7):
        ans += k%(10)
        k -= k%(10)
        k = k//10
    
    
    if ans == N:
        lst.append(i)
        
            
if len(lst) == 0:
    print(0)
else:            
    print(min(lst))