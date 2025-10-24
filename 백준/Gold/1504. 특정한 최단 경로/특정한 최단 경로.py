##다익스트라 쓰는데 두개의 지정된 정점을 지나서 종점에도달해야함
## 1, v1 
import heapq

N, E = map(int,input().split())

path = [[] for _ in range (N+1)]

for _ in range (E):
    a,b,c = map(int,input().split())
    path[a].append((b,c))
    path[b].append((a,c))

v1, v2 = map(int,input().split())


def dijkstra(start, end):
    INF = int(1e9)
    key = [INF] * (N+1)

    heap = []
    heapq.heappush(heap, (0, start))
    key[start] = 0
    
    while heap:
        cost, now = heapq.heappop(heap)
        if key[now] < cost:
            continue
        
        for next_node, next_cost in path[now]:
            new_cost = cost + next_cost
            if new_cost < key[next_node]:
                key[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))              
    
    return key[end]

temp1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N) 
temp2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)


if temp1 >= int(1e9) and temp2 >= int(1e9):
    print(-1)
else:
    print(min(temp1,temp2))