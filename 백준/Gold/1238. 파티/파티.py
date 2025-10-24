import heapq

N, M, X = map(int,input().split())

time = [[] for _ in range (N+1)]

for _ in range (M):
    a,b,c = map(int,input().split())
    time[a].append((b,c))
    
def dijkstra(start, end):
    INF = int(1e9)
    key = [INF] * (N+1)
    
    heap = []
    heapq.heappush(heap, (0, start))
    key[start] = 0
    
    while heap:
        cost, now = heapq.heappop(heap)
        
        if cost > key[now]:
            continue
        
        for next_node, next_cost in time[now]:
            new_cost = next_cost + cost
            if new_cost < key[next_node]:
                key[next_node] = new_cost
                heapq.heappush(heap, (new_cost, next_node))
                
    return(key[end])

temp = 0

for i in range (1, N+1):
    ans = dijkstra(i, X) + dijkstra(X, i)
    if ans > temp:
        temp = ans

print(temp)    
        