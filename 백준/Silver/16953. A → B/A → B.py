N, K= map(int,input().split())

ans = 1

while True:
    if K == N:
        print(ans)
        break
    if K < N:
        print(-1)
        break

    if K % 2 == 0:
        K = K//2
        ans += 1
    elif K % 10 == 1:
        K = (K-1)//10
        ans += 1
    else:
        print(-1)
        break
    
