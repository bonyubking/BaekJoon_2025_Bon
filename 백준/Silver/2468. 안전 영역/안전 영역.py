from collections import deque

N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]
max_height = max(map(max, land))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, h, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if (not visited[nx][ny]) and land[nx][ny] > h:
                    visited[nx][ny] = True
                    q.append((nx, ny))


answer = 0
for h in range(max_height + 1):  
    visited = [[False] * N for _ in range(N)]
    safe = 0
    for i in range(N):
        for j in range(N):
            if land[i][j] > h and not visited[i][j]:
                safe += 1
                bfs(i, j, h, visited)
    answer = max(answer, safe)

print(answer)
