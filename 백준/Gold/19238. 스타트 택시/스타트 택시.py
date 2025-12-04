import copy
from collections import deque

N,M,fuel = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

start_map = [list(map(int,input().split())) for _ in range(N)]
end_map = copy.deepcopy(start_map)
ans = 0

start_x, start_y = map(int,input().split())
start_x -=1
start_y -=1
end_passenger = [0,0]

for i in range (2, M+2):
    a,b,c,d = map(int,input().split())
    start_map[a-1][b-1] = i
    end_map[c-1][d-1] = i
    end_passenger.append((c-1,d-1))


def start_bfs(x,y,cur_fuel):
    
    if start_map[x][y] >= 2:
        return cur_fuel, x,y, start_map[x][y]
    
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    
    passe = []
    min_dist = int(1e9)

    while q:
        x,y = q.popleft()
        dist = visited[x][y]
        
        if min_dist < dist:
            break
        for i in range (4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==-1 and start_map[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append((nx, ny))            
                    
                    if start_map[nx][ny]>=2:
                        passe.append((visited[nx][ny],nx,ny,start_map[nx][ny]))
                        min_dist = visited[nx][ny]


    if not passe:
        return -1, -1, -1, -1

    passe.sort()
    dist, nx,ny, cust = passe[0]

    if cur_fuel < dist:
        return -1, -1, -1, -1

    return cur_fuel-dist, nx,ny ,cust



def end_bfs(x,y,cur2_fuel,dest_x, dest_y):

    visited = [[-1] * N for _ in range (N)]
    q = deque([(x,y)])
    visited[x][y] = 0
    
    if (x, y) == (dest_x, dest_y):
        return cur2_fuel
    
    while q:
        x,y = q.popleft()
        dist = visited[x][y]
        
        if (x, y) == (dest_x, dest_y):
            if cur2_fuel < dist:    
                return -1
            return cur2_fuel + dist

        for i in range (4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==-1 and end_map[nx][ny]!=1:
                    visited[nx][ny] = visited[x][y]+1
                    q.append((nx, ny))
    return -1  
    


for _ in range (M):
    
    new_fuel,nx,ny,cust = start_bfs(start_x,start_y,fuel)
    if new_fuel < 0 or cust == -1:
        print(-1)
        exit()
    start_map[nx][ny]=0
    dest_x,dest_y = end_passenger[cust]
    
    fuel = end_bfs(nx,ny,new_fuel,dest_x,dest_y)
    if fuel < 0:
        print(-1)
        exit()    
    start_x, start_y = dest_x, dest_y
    end_map[dest_x][dest_y] = 0
    
        
print(fuel)