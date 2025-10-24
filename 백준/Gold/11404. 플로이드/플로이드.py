import heapq

n = int(input())
m = int(input())

bus = [[] for _ in range (n+1)]

for _ in range (m):
    a,b,c = map(int,input().split())
    bus[a].append((b,c))



def dijkstra(start):
    
    INF = int(1e9)
    ans = [INF] * (n+1)
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
                heapq.heappush(heap, (new_cost, next_node))
    
    for i in range(len(ans)):
        if ans[i] == INF:
            ans[i] = 0
            
    return(ans)

for i in range (1, n+1):
    print(*dijkstra(i)[1:]) ## 리스트 요소를 공백으로출력(*) , 두번쨰항부터출력 ([1:])