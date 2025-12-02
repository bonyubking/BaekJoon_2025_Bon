from collections import deque
M,N = map(int,input().split())

box = [[] * M for _ in range (N)]
visited = [[0] * M for _ in range(N)]

for i in range (N):
    temp = list(map(int,input().split()))
    box[i]=temp
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q=deque()
    for i in range (N):
        for j in range (M):
            if box[i][j] == 1:
                q.append((i,j))

    while q:
        x,y = q.popleft()
        for i in range (4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if box[nx][ny]==0:
                    q.append((nx,ny))
                    box[nx][ny]=box[x][y]+1
                     
                
bfs()

result=0

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, box[i][j])

print(result-1)