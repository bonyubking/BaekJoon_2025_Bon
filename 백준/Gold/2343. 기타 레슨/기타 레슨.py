N, M = map(int,input().split())

videos = list(map(int,input().split()))

start, end = max(videos), sum(videos)
ans = 0

while start <= end:
    
    mid = (start + end) // 2
    time = 0
    cnt = 1
    
    for i in videos:
        if time + i > mid:
            cnt += 1
            time = 0
        time += i
    
    if cnt <= M:
        ans = mid
        end = mid - 1
    
    else:
        start = mid + 1

print(ans)
        
        
        