M = int(input())
N = int(input())
lst = []

for i in range(M,N+1):
    cnt = 0
    if i>1:
        for k in range(2,i):
            if i % k == 0:
                cnt += 1
                break;
        
        if cnt == 0:
            lst.append(i)   


if len(lst) < 1:
    print(-1)

else:
    print(sum(lst))
    print(min(lst))