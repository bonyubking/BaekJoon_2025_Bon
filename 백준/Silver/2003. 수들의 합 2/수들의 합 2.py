N, M = map(int,input().split())

num = list(map(int,input().split()))

l, r = 0, 0
ans = 0
temp = 0


for r in range (N):
    temp+= num[r]
    
    while temp > M and r > l:
        temp -= num[l]
        l += 1
         
    if temp == M:
        ans += 1
        

print(ans)