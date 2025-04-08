N, M = map(int,input().split())

lst=[]
cnt=[]

for i in range(N):
    lst.append(input())
    
for i in range(N-7):
    for j in range(M-7):
        white = 0
        black = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if lst[k][l]!= 'W':
                        white+=1
                    else:
                        black+=1
                else:
                    if lst[k][l]!='W':
                        black+=1
                    else:
                        white+=1
                        
        cnt.append(min(black,white))
        
print(min(cnt))