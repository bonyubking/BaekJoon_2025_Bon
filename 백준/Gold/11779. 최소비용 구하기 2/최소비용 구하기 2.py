import heapq

n = int(input())
m = int(input())

bus = [[] for _ in range (n+1)]

for _ in range (m):
    a,b,c = map(int,input().split())
    bus[a].append((b,c))

start, end = map(int,input().split())


def dijkstra(start, end):
    INF = int(1e9)
    ans = [INF] * (n+1)
    prev = [0]*(n+1)
    heap = []
    heapq.heappush(heap, (0, start))        
    ans[start] = 0

    while heap:
        cost, now = heapq.heappop(heap)
        if cost > ans[now]:
            continue
        
        for next_node, next_cost in bus[now]:
            new_cost = cost + next_cost
            if new_cost < ans[next_node]:
                ans[next_node] = new_cost
                prev[next_node] = now
                heapq.heappush(heap, (new_cost, next_node))
    # 경로 재구성
    path = []
    cur = end
    while cur != 0:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    return ans[end], path
    

distance, path = dijkstra(start, end)
print(distance)
print(len(path))
print(*path)
                