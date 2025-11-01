import sys
from collections import deque
## 위상 정렬을 하돼 같은 차수에서는 빌드시간이 가장큰놈을 빌드시간에 더해줘야할거같은데

T = int(input())

for _ in range (T):
    N, K = map(int, input().split())
    build = list(map(int, input().split()))
    time = [[] for _ in range (N)] 
    count = [0] * N  ## 위상정렬 진입차수용
    for _ in range (K):
        a, b = map(int, input().split())
        time[(a-1)].append((b-1))
        count[b-1] += 1
        
    W = int(input()) - 1
    finish = [0] * N ## 총빌드타임
    queue = deque()

    
    for i in range(N):
        if count[i] == 0:
            queue.append(i)
            finish[i] = build[i]
    
    while queue:
        key = queue.popleft()
        
        for i in time[key]:
            count[i] -= 1
            finish[i] = max(finish[i], finish[key]+build[i])
            if count[i] == 0:
                queue.append(i)
                
                
    print(finish[W])
    


    
    