from collections import deque

N = int(input())

land = []
ans = 0

for _ in range (N):
    lst = list(map(int,input().split()))
    land.append(lst)
    
def bfs(map, height):
    max_land = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[0] * N for _ in range (N)]
    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and map[i][j] > height:
                visited[i][j] = 1
                max_land+=1
                q = deque([(i,j)])

                while q:
                    x, y = q.popleft()
                    for k in range (4):
                        nx = x+dx[k]
                        ny = y+dy[k]
                        
                        if 0<=nx<N and 0<=ny<N:
                            if visited[nx][ny] == 0 and map[nx][ny] > height:
                                visited[nx][ny] = 1
                                q.append((nx,ny))
        
    return max_land

for i in range (0, 101):
    ans = max(ans, bfs(land, i))

print(ans)
    

    