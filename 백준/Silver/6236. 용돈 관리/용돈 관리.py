## 현우 N일동안 용돈리스트 받아오고 M번만 쓰기로함
## 100 400 300 100 인데 K가 300이라고 치면 
## 첫날에 100 쓰고 200남고
## 둘쨰날에 400필요한데 200뿐이니까 이러면안된다 무조건 K값이 max(amt) 보다는커야한다
## K가 600이라고치면 첫날에 100 둘쨰날에 400까진문제없고
## 셋쨰날에 300써야하는데 100밖에없으니까
## K를 다시 600으로만들어야함
## 앞에서 풀었듯이 최대값 end는 sum으로 하면될듯



N, M = map(int,input().split())

amt = []

for i in range (N):
    key = int(input())
    amt.append(key)
    
start, end = max(amt), sum(amt)


while start <= end:
    mid = (start + end) // 2
    cnt = 1 ## 일단 이걸 인출횟수라고생각
    money = 0
    
    for i in amt:
        if money + i > mid: ## 돈다씀
            cnt += 1
            money = 0
        money += i
    
    if cnt <= M:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(ans)

