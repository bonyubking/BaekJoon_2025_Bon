from collections import deque


M, N = map(int,input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

graph = [] 

visited=[False]*(N+1)

Q = deque()

for _ in range(N):
    key = list(map(int, input().split()))
    graph.append(key)


for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            Q.append([i,j])
            

    
while Q:
        length = len(Q)
        for _ in range(length):
            i,j = Q.popleft()

            for k in range (4):
                di = dr[k] + i
                dj = dc[k] + j
                
                if dj >= 0 and dj < M and di < N and di >= 0 and graph[di][dj] == 0:
                    graph[di][dj] = graph[i][j] + 1
                    
                    Q.append([di, dj])
ans = 0    
               
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            
            exit()
            
    ans = max(ans, max(i))
    
print(ans - 1)