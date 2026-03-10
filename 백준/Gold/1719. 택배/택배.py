from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())


loads = [[] for _ in range(N+1)]
anslst = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, time = map(int, input().split())
    loads[a].append((b, time))
    loads[b].append((a, time))
    

def bfs(start):
    q = deque()
    dp = [1e9] * (N+1)
    dp[start] = 0
    bestlst = [i for i in range (N+1)] 
    q.append(start)
    
    while q:
        temp = q.popleft()
        for key, value in loads[temp]:
            new_time = dp[temp] + value
            
            if new_time < dp[key]:
                dp[key] = new_time
                if temp != start:
                    bestlst[key] = bestlst[temp]
                q.append(key)
                
    bestlst[start] = '-'
    return bestlst

for i in range (1, N+1):
    templst = bfs(i)
    print(*templst[1:])
            
        
    
