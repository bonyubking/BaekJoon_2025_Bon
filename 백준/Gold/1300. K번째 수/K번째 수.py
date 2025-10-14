## N*N 배열 A 인데 일차원으로만들어서 오름차순정렬한다고침

## 3*3 배열이라치면
## 1 2 3    1 2 2 3 3 4 6 6 9
## 2 4 6 
## 3 6 9

## 4*4라고치면

## 1 2  3  4   5        1 2 2 3 3 4 4 4 6 6 8 8 9 12 12 16
## 2 4  6  8   10       
## 3 6  9  12  15
## 4 8  12 16  20
## 5 10 15 20  25

 
N = int(input())
K = int(input())

start, end = 1, K
ans = 0 

while start <= end:
    mid = (start + end) // 2
    cnt = 0 ## 작은 숫자 갯수 
    
    for i in range (1, N+1):
        cnt += min(mid // i, N)
    
    if cnt >= K:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(ans)