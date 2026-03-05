from collections import deque


N = int(input())

maps = []
for i in range (N):
    lst = list(map(int,input().split()))
    maps.append(lst)

visited = [[0] * N for _ in range(N)]    

dx = [1,0,-1,0]
dy = [0,1,0,-1]
landnum = 0

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1 and visited[i][j] == 0:
            landnum+=1
            visited[i][j] = landnum
            q=deque([(i,j)])
            
            while q:
                x, y = q.popleft()
                for h in range (4):
                    nx = x+dx[h]
                    ny = y+dy[h]
                    if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and maps[nx][ny] == 1:
                        visited[nx][ny] = landnum
                        q.append([nx,ny])

ans = 1e9

for s in range(1, landnum + 1):
    dist = [[-1]*N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if visited[i][j] == s:
                q.append((i, j))
                dist[i][j] = 0
                
    while q:
        x, y = q.popleft()
        if dist[x][y]+1 > ans:
            break
        for h in range(4):
            nx = x+dx[h]
            ny = y+dy[h]
            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

                elif visited[nx][ny] != 0 and visited[nx][ny] != s:
                    ans = min(ans, dist[x][y])
                    q.clear()
                    break;


print(ans)                                        

        