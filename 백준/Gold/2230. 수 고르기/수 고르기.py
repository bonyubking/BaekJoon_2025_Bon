import sys
N, M = map(int,sys.stdin.readline().split())


num = [int(sys.stdin.readline()) for _ in range(N)]   
num.sort()
ans = num[N-1] - num[0]

l, r = 0, 0

while r <= (N-1) and r >= l:
    
    if num[r] - num[l] < M:
        r += 1
    
    else:
        temp = num[r] - num[l]
        ans = min(ans, temp) 
        l += 1

print(ans)
            
    
    
    