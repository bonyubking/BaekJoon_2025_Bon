import sys
G = int(sys.stdin.readline())
ans = []
l, r = 1, 2

while r < 100000:
    temp = r*r - l*l
    if temp == G:
        ans.append(r)
        r += 1
    elif temp < G:
        r += 1
    else:
        l += 1

if ans:
    print(*ans, sep='\n')
else:
    print(-1)