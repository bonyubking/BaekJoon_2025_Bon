N = int(input())

lst = []
ans = 0


    
for i in range(0, N//5+1):
    temp = N-5*i
    ans += i
    if temp%3 == 0:
        j = temp//3
        lst.append(i+j)

if len(lst) == 0:
    print(-1)
else:
    print(min(lst))