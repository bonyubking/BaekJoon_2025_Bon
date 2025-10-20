N = int(input())

# 포도주시식인데

# 아까 했떤문제랑 패턴이똑같다 계단오르는거랑
# 그대신 세잔연속마실수가없음

# 그러면 N번쨰 점화식을구할떄
# dp(N-3) + N-1 + N
# dp(N-2) + N

# 이렇게비교하면될거같은데 처음에 틀렸음
# 생각해보니까 현재꺼안마실수도잇음 그런경우는 
# dp(N-1) 이네 

grape = []
dp = [0] * N

for _ in range (N):
    key = int(input())
    grape.append(key)
    
if N == 1:
    print(grape[0])

elif N == 2:
    print(grape[0] + grape[1])
    
else:
    dp[0] = grape[0]
    dp[1] = grape[0] + grape[1]
    dp[2] = max(grape[1] + grape[2], grape[0]+grape[1], grape[0]+grape[2])

    for i in range(3, N):
        dp[i] = max(dp[i-3] + grape[i-1] + grape[i], dp[i-2] + grape[i], dp[i-1])



    print(dp[N-1])
