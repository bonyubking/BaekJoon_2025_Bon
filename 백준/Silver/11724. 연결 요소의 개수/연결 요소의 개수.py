## 연결 요소 ;
##연결 요소에 속한 모든 정점을 연결하는 경로가 있어야 한다.
##다른 연결 요소에 속한 정점과 연결하는 경로가 있으면 안된다.
##BFS 1부터 돌면서 더이상 갈데없으면 +1해주면될듯
from collections import deque

N,M = map(int,input().split())

node = [[] for _ in range (N+1)]
visited = [0] * (N+1)
q = deque()
ans=0

for _ in range (M):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)
    
for i in range (1, N+1):
    if visited[i] == 0:
        visited[i] = 1
        q.append(i)
        while q:
            temp = q.popleft()
            for key in node[temp]:
                if visited[key] == 0:
                    visited[key] = 1
                    q.append(key)
        ans+=1

print(ans)