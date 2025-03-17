N = int(input())
friendList = []
manList = [[0] * N for i in range(N)]

for i in range(N):
    key = input()
    friendList.append(key)
    
    

for i in range(N):
    for j in range(N):
        for k in range(N):
            if k == j:
                continue
        
            if friendList[j][k] == 'Y' or (friendList[j][i] == 'Y' and friendList[i][k] == 'Y'):
                manList[j][k] = 1


cnt = 0

for key in manList:
    cnt = max(sum(key), cnt)
    
    
print(cnt)