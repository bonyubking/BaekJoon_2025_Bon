N, M = map(int,input().split())

anslist = []
tempdict = dict()
temp = 1

for _ in range (N):
    key = input().strip()
    if len(key) >= M:
        anslist.append(key)
        
anslist.sort() 

for i in range(len(anslist)-1):
    
    if anslist[i+1] == anslist[i]:
        temp += 1
    else:
        tempdict[anslist[i]] = temp
        temp = 1
        
tempdict[anslist[-1]] = temp

ans = sorted(tempdict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in ans:
    print(i[0])

