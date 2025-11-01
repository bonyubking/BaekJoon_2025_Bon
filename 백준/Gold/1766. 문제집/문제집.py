## 위상정렬하는데 같은위상차수이면 작은놈이앞에와야하고 있는거다풀어야함 
import heapq
N, M = map(int,input().split())

probs = [[] for _ in range(N+1)]
count = [0] * (N+1)
ans = []

for _ in range(M):
    a, b = map(int,input().split())
    probs[a].append(b)
    count[b] += 1

queue = []

for i in range(1, N+1):
    if count[i] == 0:
        heapq.heappush(queue, i)

while queue:
    key = heapq.heappop(queue)
    ans.append(key)
    for i in probs[key]:
        count[i] -= 1
        if count[i] == 0:
            heapq.heappush(queue, i)

print(*ans)  # 출력: 1 2 3 4
