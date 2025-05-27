import heapq

N = int(input())

lst = []
cnt = 1
fin = [0]

for i in range(N):
    lst.append(list(map(int,input().split())))
    
lst.sort()



heap = []

for s, e in lst:
    if heap and heap[0] <= s:
        heapq.heapreplace(heap, e)   
    else:
        heapq.heappush(heap, e) 

print(len(heap)) 