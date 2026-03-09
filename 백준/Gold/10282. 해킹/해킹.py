from collections import deque

t = int(input())
for _ in range (t):
    ans = 0
    max_time = 0
    n, d, c = map(int,input().split())

    comp = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, time = map(int, input().split())
        comp[b].append((a, time))  

    q = deque([c])
    dp = [1e9] * (n+1)
    dp[c] = 0

    
    while q:
        com = q.popleft()
        
        for index, time in comp[com]:

            new_time = dp[com]+time
            
            if new_time < dp[index]:
                dp[index] = new_time
                q.append(index)
  
    
    for i in range(1, n+1):
        if dp[i] != 1e9:
            ans+=1
            max_time = max(max_time, dp[i])
       
    print(ans, max_time)
