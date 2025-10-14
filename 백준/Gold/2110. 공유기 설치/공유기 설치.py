## N개 일직선상에있음 순서대로
## C개를 적절하게 설치하는데 가장 인접한 공유기 거리 최대가되어야한다
## 최대한 띄엄띄엄 설치를 해라는뜻
## 1 2 8 4 9 에 3대설치하면 답이 3이니까

## 1 2 4 8 9 로 정렬해서 저장하고 
## 1 4 9 에 설치하는경우가 젤띄엄띄엄인듯


N, C = map(int,input().split())
home = []

for i in range (N):
    key = int(input())
    home.append(key)
    
home.sort()

start, end =  1, max(home)-min(home)

while start <= end:
    mid = (start + end) // 2
    last = home[0] # 마지막 설치한집
    cnt = 1 # 공유기갯수
    
    for i in home: ## 이거는 거리로해야돼니까 in range써서해본다일단
        if i - last >= mid:
            cnt += 1
            last = i
    
    if cnt >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)