## N 1씩키우면서 안전영역 그떄그떄 BFS로계산해서 MAX값 비교
from collections import deque

N = int(input())
ans = 1
land = [[] for _ in range (N)]

for i in range (N):
    temp = list(map(int,input().split()))
    land[i] = temp
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(x,y, key, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if land[nx][ny] > key and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    
for key in range(1, 101):
    visited = [[0]*N for _ in range(N)]
    temp1 = 0

    for i in range(N):
        for j in range(N):
            if land[i][j] > key and visited[i][j] == 0:
                bfs(i, j, key, visited)
                temp1 += 1

    ans = max(ans, temp1)
    
print(ans)