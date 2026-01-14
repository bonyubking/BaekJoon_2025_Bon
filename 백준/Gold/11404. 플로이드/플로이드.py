N = int(input())
M = int(input())

cost = [[1e9] * N for _ in range (N)]

for i in range(N):
    cost[i][i] = 0

for _ in range (M):
    a,b,c = map(int,input().split())
    if cost[a-1][b-1] != 0:
        cost[a-1][b-1] = min(cost[a-1][b-1], c)
    else:
        cost[a-1][b-1] = c


for k in range(N):
    for i in range(N):
        for j in range(N):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(N):
    for j in range(N):
        if cost[i][j] == 1e9:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()