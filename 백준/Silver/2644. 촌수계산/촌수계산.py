from collections import deque

N = int(input())

X, Y = map(int,input().split())

M = int(input())

graph = [[] for _ in range(N+1)] 

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    

    
def bfs(x, y):
    
    visited = [False] * (N + 1)
    q = deque([x])
    visited[x] = True
    cnt = 0
    
    while q:
        for _ in range(len(q)):
            u = q.popleft()
            if u == y:
                return cnt
            for i in graph[u]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
        
        cnt+=1
                
    return -1

print(bfs(X,Y))