N = int(input())
A = [0 for i in range(N)]
B = [0 for i in range(N)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0

A.sort()
B.sort()

for i in range(N):
    S = A[N-1-i]*B[i]
    ans = ans + S
    
print(ans)
