from collections import deque

M,N,K = map(int,input().split())

q=deque()
rec = []
ans = 0

visited = [[0] * N for _ in range(M)]

for _ in range (K):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range (y1, y2):
            visited[j][i] = 1

dx = [1,0,-1,0]
dy = [0,1,0,-1]

landlst = []

for i in range (M):
    for j in range (N):
        if visited[i][j] == 0:
            ans+=1
            visited[i][j] = 1
            q = deque([(i, j)])
            land = 1
            
            while q:
                x,y = q.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0<=nx<M and 0<=ny<N:
                        if visited[nx][ny]==0:
                            visited[nx][ny]=1
                            q.append((nx,ny))
                            land+=1
            
            landlst.append(land)

landlst.sort()
             
print(ans)
print(*landlst) 
