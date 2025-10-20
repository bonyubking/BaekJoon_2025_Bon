# 계단오르기

# 한번에 한개 or 두개 갈수있음
# 한개를 두번은못감

# 한개를 한번갔으면 그다음은 무조건두개가야함
# 다음거랑 다다음거랑 비교해서
# 마지막 계단은 무조껀밟아야하니까 마지막계단부터 출발한다고생각

N = int(input())
score = []
dp = [0] * N

for _ in range (N):    
    key = int(input())
    score.append(key)

if N == 1:
    print(score[0])
elif N == 2:
    print(score[0] + score[1])
else:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])

    for i in range (3, N):
        dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])

    print(dp[N-1])    
