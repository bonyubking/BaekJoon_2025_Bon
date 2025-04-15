N = int(input())

Nset = set(map(int,input().split()))

M = int(input())

Mlist = list(map(int,input().split()))

Keyset = set()

Nset 
        
            
for i in range(len(Mlist)):
    if Mlist[i] in Nset:
        Mlist[i] = 1
    else:
        Mlist[i] = 0
        
print(' '.join(map(str,Mlist)))