N, M = map(int,input().split())

Nlist = []
Mlist = []
Anslist = []

for i in range (N):
    Nlist.append(list(map(int,input().split())))


for i in range (N):
    Mlist.append(list(map(int,input().split())))    


for i in range (N):
    key = []
    for j in range (M):
        key.append(Nlist[i][j] + Mlist[i][j])  
    Anslist.append(key)  
        

for i in range (N):
    for j in range(M):
        print(Anslist[i][j], end = " ")
        
    print()