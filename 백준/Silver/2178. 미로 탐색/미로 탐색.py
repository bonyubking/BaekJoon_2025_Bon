from collections import deque


N, M = map(int,input().split())

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

graph = [] 

for _ in range(N):
    key = list(map(int, input().strip()))
    graph.append(key)
    
visited = [[False]*M for _ in range(N)]
    

Q = deque()
Q.append((0,0))
visited[0][0] = True
ans = 1

while Q:
    
    for _ in range(len(Q)):
        i,j = Q.popleft()
        
        if (i,j) == (N-1, M-1):
            print(ans)
            exit()

        for k in range (4):
            di = dr[k] + i
            dj = dc[k] + j
                    
            if 0 <= di < N and 0 <= dj < M and graph[di][dj] == 1 and not visited[di][dj]:
                    
                visited[di][dj] = True
                Q.append([di, dj])
    
    ans += 1
    
    
print(ans)