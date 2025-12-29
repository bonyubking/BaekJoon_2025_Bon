X = int(input())

if X <= 1:
    print(0)

elif X <= 3:
    print(1)
    
else: 

    dp = [0] * (X+1)
    dp[0], dp[1], dp[2], dp[3] = 0, 0, 1, 1


    for i in range(4, X+1):
        
        if i % 3 == 0 and i % 2 == 0:
            A = min(dp[i//3],dp[i//2],dp[i-1])+1
            dp[i] = A
        
        elif i % 2 == 0:
            A = min(dp[i//2], dp[i-1])+1
            dp[i] = A
            
        elif i % 3 == 0:
            A = min(dp[i//3], dp[i-1])+1
            dp[i] = A
            
        else:
            A = dp[i-1]+1
            dp[i] = A

    print(dp[X])