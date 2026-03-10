import sys
import heapq
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())
see = list(map(int,input().split()))
see[N-1] = 0

templst = []
loads = [[] for _ in range(N)]

for i in range(M):
    a, b, time = map(int, input().split())
    if see[a] == 0 and see[b] == 0:
        loads[a].append((b, time))
        loads[b].append((a, time))
        
dp = [10**18] * N
q = []
heapq.heappush(q, (0, 0))
dp[0] = 0

while q:
    cur_cost, cur_node = heapq.heappop(q)

    if dp[cur_node] < cur_cost:
        continue
        
    for next_cost, next_node in loads[cur_node]:
        new_cost = cur_cost + next_node
        if new_cost < dp[next_cost]:
            dp[next_cost] = new_cost
            heapq.heappush(q, (new_cost, next_cost))

if dp[N-1] == 10**18:
    print(-1)
else:
    print(dp[N-1])