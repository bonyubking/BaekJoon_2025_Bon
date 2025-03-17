N = int(input())
nList = []
cnt = 0
keynum = -1

for i in range(N):
    key = int(input())
    nList.append(key)
    
    
nList.sort()


for i in range(0, len(nList)-2):
    if nList[i] + nList[i+1] > nList[i+2]:
        keynum = i
        
    
if keynum == -1:
    print('-1')
    
else:
    print(nList[keynum]+nList[keynum+1]+nList[keynum+2])