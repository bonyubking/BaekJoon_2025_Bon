N = int(input())


dis = list(map(int,input().split()))

price = list(map(int,input().split()))

for i in range (0, N-1):
    if price[i] < price[i+1]:
        price[i+1] = price[i]
            
cnt = 0

for i in range (0, N-1):
    cnt += dis[i]*price[i]           

print(cnt)