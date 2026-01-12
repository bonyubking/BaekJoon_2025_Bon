N, M = map(int,input().split())

friends = [[1e9] * (N+1)  for _ in range (N+1)]
target = 1e9

for i in range(1, N+1):
    friends[i][i] = 0
    
for _ in range (M):
    a,b = map(int,input().split())
    friends[a][b] = 1
    friends[b][a] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            friends[i][j] = min(friends[i][j], friends[i][k] + friends[k][j])
            
for i in range (1, N+1):
    temp = 0
    for j in range (1, N+1):
        temp += friends[i][j]
    
    if temp < target:
        target = temp
        ans = i
        
print(ans)

    