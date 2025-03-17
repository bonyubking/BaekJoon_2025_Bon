# 시리얼 번호

N = int(input())

ansList = [0 for i in range(N)]
newList = []

for i in range(N):
    key = str(input().rstrip())
    num = len(key)
    s = 0
    for i in range(num):
        if key[i].isdigit():
            s += int(key[i])
    
    newList.append([num,s,key])

newList.sort()

for row in newList:
    print(row[2])