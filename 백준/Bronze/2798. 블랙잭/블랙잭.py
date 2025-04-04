N, M = map(int,input().split())

Cardlist = list(map(int,input().split()))

Cardlist.sort()
total = 0


for i in range (N-2):
    for j in range (i+1,N-1):
        for k in range (j+1,N):
            if Cardlist[i]+Cardlist[j]+Cardlist[k] <= M:
                total = max(Cardlist[i]+Cardlist[j]+Cardlist[k],total)
                


print(total)