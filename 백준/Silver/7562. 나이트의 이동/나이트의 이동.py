from collections import deque
T = int(input())

dx = [2,-2,1,-1,2,-2,1,-1]
dy = [1,-1,2,-2,-1,1,-2,2]

for _ in range (T):
    N = int(input())
    startx, starty = map(int,input().split())
    endx, endy = map(int,input().split())
    visited = [[-1] * N for _ in range (N)]
    q = deque([(startx, starty)])
    visited[startx][starty] = 0
    
    while q:
        x, y = q.popleft()
        
        if x == endx and y == endy:
            print(visited[x][y])
            break;
        
        for i in range (8):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y]+1
                q.append((nx,ny))
            


     