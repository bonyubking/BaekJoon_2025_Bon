N = int(input())

cost = []

for i in range (N):
    rgb = list(map(int,input().split()))
    cost.append(rgb)

ans = [cost[0]]

for i in range (1, N):
    alpha = min(ans[i-1][1], ans[i-1][2]) + cost[i][0]
    beta = min(ans[i-1][0], ans[i-1][2]) + cost[i][1]
    gamma = min(ans[i-1][1], ans[i-1][0]) + cost[i][2]
    ans.append([alpha, beta, gamma])

print(min(ans[N-1]))