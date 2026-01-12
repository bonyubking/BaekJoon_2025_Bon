from collections import deque
N,K = map(int,input().split())

dist = [0] * 100001

def bfs(start, target):
    q = deque()
    q.append(start)
    
    while q:
        temp = q.popleft()
        if temp == target:
            return(dist[temp])
            break;
        
        for key in (temp*2, temp-1, temp+1):
            if 0<=key<=100000 and dist[key] == 0:
                if key == temp*2:
                    dist[key] = dist[temp]
                else:
                    dist[key] = dist[temp]+1
                q.append(key)
                
ans = bfs(N,K)

print(ans)
