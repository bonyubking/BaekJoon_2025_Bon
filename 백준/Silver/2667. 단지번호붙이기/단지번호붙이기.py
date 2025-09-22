from collections import deque

N = int(input())

graph = [] 

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(N):
    key = list(map(int, input().strip()))
    graph.append(key)
    

anslist = []
visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            Q = deque()
            Q.append((i,j))
            visited[i][j] = True
            num = 1
            
            while Q:         
                x,y = Q.popleft()
                for k in range (4):
                    dx = dr[k] + x
                    dy = dc[k] + y
                                
                    if 0 <= dx < N and 0 <= dy < N and graph[dx][dy] == 1 and not visited[dx][dy]:
                        visited[dx][dy] = True
                        Q.append([dx, dy])
                        num += 1

            anslist.append(num)

anslist.sort()
print(len(anslist))
for n in anslist:
    print(n)
