## BFS 사용해서 구역 한개당 ans += 1
from collections import deque

T = int(input())


def bfs(x,y):
    q = deque()
    q.append((x,y))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for j in range(4):
            nx = x+dx[j]
            ny = y+dy[j]
            if 0 <= nx < N and 0 <= ny < M:
                if baechu[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    
for _ in range (T):
    
    M,N,K = map(int,input().split())

    baechu = [[0] * M for _ in range (N)]
    visited = [[0] * M for _ in range (N)]
    ans = 0
    
    for _ in range(K):
        a,b = map(int,input().split())
        baechu[b][a] = 1
    
    for i in range (N):
        for j in range(M):
            if baechu[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                ans+=1
    print(ans)
        



