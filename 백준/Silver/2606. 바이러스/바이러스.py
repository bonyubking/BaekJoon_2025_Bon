N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)] 

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    

virus = [False] * (N+1)

def dfs(x):
    virus[x] = True
    count = 0
    for i in graph[x]:
        if not virus[i]:
            dfs(i)

dfs(1)

cnt = sum(virus) - 1
print(cnt)

