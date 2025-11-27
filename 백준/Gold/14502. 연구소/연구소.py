import copy
N, M = map(int,input().split())
from collections import deque

maps = [list(map(int,input().split())) for _ in range (N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

virus_positions = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            virus_positions.append((i, j))


ans = 0

def bfs():
    global ans
    cur_safe = 0
    temp = copy.deepcopy(maps)
    bug = deque(virus_positions)
    
    while bug:
        x, y = bug.popleft()
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                bug.append((nx,ny))
    
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                cur_safe += 1
                            
    ans = max(cur_safe,ans)
                
            
def makewall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range (N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                makewall(cnt+1)
                maps[i][j] = 0

makewall(0)

print(ans)










            