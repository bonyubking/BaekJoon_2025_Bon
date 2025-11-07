N, M = map(int,input().split())


num = [int(input()) for _ in range(N)]   
num.sort()
ans = max(num) - min(num)

l, r = 0, 0

while r <= (N-1):
    
    if num[r] - num[l] < M:
        r += 1
    
    else:
        temp = num[r] - num[l]
        ans = min(ans, temp) 
        l += 1
    
    if l > r:
        break

print(ans)
            
    
    
    