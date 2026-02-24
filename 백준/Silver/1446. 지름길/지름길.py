## 

N, D = map(int,input().split())

ans = 0
load = []


for _ in range (N):
    loadlst = list(map(int,input().split()))
    if loadlst[1]-loadlst[0] > loadlst[2] and loadlst[1] <= D:
        load.append(loadlst)
    
load.sort()

dp = [i for i in range(D+1)]

for i in range (D+1):
    dp[i] = min(dp[i-1]+1, dp[i])
    
    for a,b,c in load:
        if a == i:
            dp[b] = min(dp[a]+c, dp[b])

print(dp[D])
    
    