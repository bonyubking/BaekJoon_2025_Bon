

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)] 

count = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited=[False]*(N+1)


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)
            
            
for i in range (1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)
        
print(count)