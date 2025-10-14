K, N = map(int,input().split())
lans = []

for i in range (K):
    key = int(input())
    lans.append(key)
    
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2 
    cnt = 0
     
    for i in lans:
        cnt += i // mid 
        
    if cnt >= N: 
        start = mid + 1
    else:
        end = mid - 1
        
print(end)
