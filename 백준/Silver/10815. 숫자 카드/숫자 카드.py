N = int(input())

Nset = set(map(int,input().split()))

M = int(input())

Mlist = list(map(int,input().split()))
Mset = set(Mlist)

Keyset = set()


Keyset = Nset & Mset
        
            
for i in range(len(Mlist)):
    if Mlist[i] in Keyset:
        Mlist[i] = 1
    else:
        Mlist[i] = 0
        
print(' '.join(map(str,Mlist)))