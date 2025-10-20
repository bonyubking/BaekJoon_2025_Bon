# 미로 크기받고 사탕갯수받고
# 이동은 오른쪽, 아래, 대각선아래 세가지경우로가능

# 막연하게생각했을떄 대각선아래는 왜고려야해야돼는지 모르겠음 그냥 오른쪽으로가고아래가는게 무조건 사탕이 같건가많을텐데

# 그래서 오른쪽으로가는거랑 아래로가는거만 생각할래

# N,M까지올떄 최대값 -> (N-1),M  이랑 N , M-1까지의최대값중에 큰거 + N,M값


N, M = map(int,input().split())

candy = []
dp = [[0 for _ in range(M)] for _ in range(N)]

for i in range (N):
    key = list(map(int,input().split()))
    candy.append(key)
    
dp[0][0] = candy[0][0]



for i in range(1, N):
    dp[i][0] = dp[i-1][0] + candy[i][0]

for j in range(1, M):
    dp[0][j] = dp[0][j-1] + candy[0][j]


for i in range(1, N):
    for j in range(1, M):    
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + candy[i][j]
    
print(dp[N-1][M-1])