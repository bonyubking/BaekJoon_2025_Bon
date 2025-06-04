from collections import deque


N, M = map(int,input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

graph = [] 



for _ in range(N):
    key = list(map(int, input().strip()))
    graph.append(key)

Q = deque()
Q.append((0,0))

while Q:
    i,j = Q.popleft()

    for k in range (4):
        di = dr[k] + i
        dj = dc[k] + j
                
        if 0 <= di < N and 0 <= dj < M and graph[di][dj] == 1:
                
            graph[di][dj] = graph[i][j] + 1
            Q.append([di, dj])
                    


print(graph[N-1][M-1])