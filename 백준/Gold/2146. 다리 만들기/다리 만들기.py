from collections import deque


N = int(input())

maps = []
for i in range (N):
    lst = list(map(int,input().split()))
    maps.append(lst)

visited = [[0] * N for _ in range(N)]
dist = [[1e9]*N for _ in range(N)]    

dx = [1,0,-1,0]
dy = [0,1,0,-1]
landnum = 0

templst = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == 0:
            dist[i][j] = 0
            landnum+=1
            visited[i][j] = landnum
            q=deque([(i,j)])
            templst.append([i,j])
            
            while q:
                x, y = q.popleft()
                for h in range (4):
                    nx = x+dx[h]
                    ny = y+dy[h]
                    if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and maps[nx][ny] == 1:
                        visited[nx][ny] = landnum
                        q.append([nx,ny])
                        templst.append([nx,ny])
                        dist[nx][ny] = 0

ans = 1e9

for a,b in templst:
    
    q2 = deque([(a,b)]) 
      
    while q2:
        x, y = q2.popleft()
        
        if dist[x][y]+1 > ans:
            continue
        
        for h in range(4):
            nx = x+dx[h]
            ny = y+dy[h]
            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] == 0 and dist[nx][ny] > dist[x][y]+1:
                    dist[nx][ny] = dist[x][y] + 1
                    q2.append((nx, ny))

                elif visited[nx][ny] != 0 and visited[nx][ny] != visited[a][b]:
                    ans = min(ans, dist[x][y])
                    break;

print(ans)

                                  

        