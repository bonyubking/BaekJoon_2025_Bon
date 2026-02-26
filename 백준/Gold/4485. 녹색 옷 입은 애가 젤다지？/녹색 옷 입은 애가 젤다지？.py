from collections import deque
problem = 1
while True:
    ans = 0
    cave = []
    N = int(input())
    
    dist = [[1e9] * N for _ in range(N)]
    
    if not N:
        break;
    
    for _ in range (N):
        lst = list(map(int,input().split()))
        cave.append(lst)
        
    dist[0][0] = cave[0][0]
    
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]

        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                nd = dist[x][y] + cave[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    q.append((nx, ny))

    print(f"Problem {problem}: {dist[N-1][N-1]}")
    problem += 1


