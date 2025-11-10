N = int(input())
num = []


if N < 2:
    print(0)
    exit()

is_prime = [True] * (N + 1)
is_prime[0], is_prime[1] = False, False

for i in range(2, int(N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

num = [i for i in range(2, N + 1) if is_prime[i]]
        
dis = len(num)
l, r, ans, temp = 0, 0, 0, 0

for r in range(dis):
    temp += num[r]
    while temp > N and l <= r:
        temp -= num[l]
        l += 1
    if temp == N:
        ans += 1
    
print(ans)
        
        