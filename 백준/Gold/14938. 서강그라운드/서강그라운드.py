from collections import deque

temp = 0
N, M, R = map(int,input().split())

items = list(map(int,input().split()))
loads = [[0] * (N+1) for _ in range (N+1)]

for _ in range (R):
    a, b, c = map(int,input().split())
    loads[a][b] = c
    loads[b][a] = c

for i in range (1, N+1):
    ans = items[i-1]
    q = deque([(i,0)])
    visited = [0] * (N+1)
    dp = [1e9] * (N+1)
    visited[i] = 1
    dp[i] = 0
    
    while q:
        key, dist = q.popleft()
        for j in range (1, N+1):
            
            new_dist = dist + loads[key][j]
            
            if 0 < loads[key][j] and new_dist < dp[j] and new_dist <= M:
                if visited[j] == 0: 
                    visited[j] = 1
                    ans += items[j-1]
                dp[j] = new_dist
                q.append((j, new_dist))
                
    
    temp = max(ans, temp)

print(temp)