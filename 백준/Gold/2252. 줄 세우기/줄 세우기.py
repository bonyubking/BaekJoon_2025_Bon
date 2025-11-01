from collections import deque

N, M = map(int,input().split())

node = [[] for _ in range(N+1)]
stack = [0] * (N+1)

for _ in range (M):
    a, b = map(int,input().split())
    node[a].append(b)
    stack[b] += 1

q = deque()
for i in range(1, N+1):
    if stack[i] == 0:
        q.append(i)
        
while q:
    key = q.popleft()
    
    for i in node[key]:
        stack[i] -= 1
        if stack[i]==0:
            q.append(i)
        
    print(key, end=" ")   
    
