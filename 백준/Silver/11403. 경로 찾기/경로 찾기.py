N = int(input())

node = [[] for _ in range(N)]
ans = [[0] * N for _ in range (N)]

for i in range (N):
    temp = list(map(int,input().split()))
    for j in range (N):
        node[i].append((temp[j]))

for i in range (N):
    for j in range(N):
        for k in range(N):
            if node[j][i] and node[i][k]:
                node[j][k] = 1

for key in node:
    print(*key)