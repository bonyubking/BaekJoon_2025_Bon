key1 = list(input().strip())
key2 = list(input().strip())

a,b = len(key1), len(key2)
dp = [[""] * (b+1) for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        if key1[i-1] == key2[j-1]:
            dp[i][j] = dp[i-1][j-1] + key1[i-1]
        else:
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]


temp = len(dp[a][b])

if temp == 0:
    print(0)
else:             
    print(temp)
    print(dp[a][b])

    