from collections import deque

N, M, V = map(int,input().split())


graph = [[] for _ in range(N+1)] 


for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


for nbrs in graph:
    nbrs.sort()
    
    
visited=[False]*(N+1)
visited_bfs=[False]*(N+1)


def dfs(x):
    visited[x] = True
    print(x, end =' ') 
    for i in graph[x]:
        if visited[i]==False: 
            dfs(i)
            

def bfs(x):
    q = deque([x])
    visited_bfs[x] = True
    while q:
        u = q.popleft()
        print(u, end=' ')
        for i in graph[u]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                q.append(i)
                



dfs(V)
print()
bfs(V)