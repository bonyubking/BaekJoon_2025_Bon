from collections import deque


N, M = map(int,input().split())

Q = deque()

Q.append((N,0))

visited = [0] * 100001

visited[N] = 1

ans = 0

while Q:

    i , ans = Q.popleft()
    
    if i == M:
        break;
    
    lst = [i+1, i-1, i*2]

    
    for j in lst:
        if 0<= j <= 100000 and visited[j] == 0:
            Q.append((j, ans+1))
            visited[j] = 1

    

print(ans)    