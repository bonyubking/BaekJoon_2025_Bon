from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    

def bfs(start):
    visited = [False] * (N+1)
    dist = [0] * (N+1)
    
    q = deque([start])
    visited[start] = True
    dist[start] = 0
    
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    
    return sum(dist[1:])


target = 1e9

for i in range (1, N+1):
    total = bfs(i)
    if total < target:
        target = total
        ans = i
        
print(ans)
        