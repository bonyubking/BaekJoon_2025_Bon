N = int(input())
M = list(map(int,input().split()))

M.sort()
ans = 0
temp = 0

for key in M:
    if key >= temp*2:
        ans += 1
        temp = key

print(ans)