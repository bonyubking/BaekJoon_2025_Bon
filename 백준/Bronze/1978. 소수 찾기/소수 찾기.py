## 소수 찾기
## 주어진 N개 중 소수가 몇개 인지

N = int(input())
lst = [0] * N
ans = 0

Key = list(map(int,input().split()))

for i in range (N):
    lst[i] = Key[i]
    
    
for key in lst:
    cnt = 0
    for j in range (1, key+1):
        if key % j == 0:
            cnt += 1
    if cnt == 2:
        ans+= 1        

print(ans)