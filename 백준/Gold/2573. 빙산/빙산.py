from collections import deque

N, M = map(int,input().split())

graph = []
year = 0

for _ in range(N):
    key = list(map(int, input().split()))
    graph.append(key)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(x, y):
    
    Q = deque()
    Q.append((x, y))
    visited[x][y] = True
    
    while Q:
        i,j = Q.popleft()
        for k in range(4):
            ni = i + dr[k]
            nj = j + dc[k]
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] > 0 and not visited[ni][nj]:
                    visited[ni][nj] = True
                    Q.append((ni, nj))
                    
while True:
    cnt = 0
    visited = [[False]*M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(i,j)
                cnt += 1
    
    if cnt == 0:
        print(0)  
        exit()
    if cnt >= 2:
        print(year)  
        exit()
    
    new_graph = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            minus = 0
            for k in range (4):
                di = dr[k] + i
                dj = dc[k] + j
                if 0 <= di < N and 0 <= dj < M and graph[di][dj] == 0:
                    minus += 1
            new_graph[i][j] =  graph[i][j] - minus
            if new_graph[i][j] < 0:
                new_graph[i][j] = 0

    graph = new_graph
    year += 1


                
    