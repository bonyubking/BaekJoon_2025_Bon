import sys

N, S = map(int,sys.stdin.readline().split())
num = list(map(int,sys.stdin.readline().split()))

l, temp, ans = 0, 0, N+1

for r in range(N):
    temp += num[r]

    while temp >= S:
        ans = min(ans, r - l + 1)
        temp -= num[l]
        l += 1
    

if ans == N+1:
    print(0)
else:
    print(ans)