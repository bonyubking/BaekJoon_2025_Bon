import sys

monNum, targetNum = map(int,sys.stdin.readline().split())
pocketMonList = {}
anslist = []

for i in range(monNum):
    poName = sys.stdin.readline().strip()
    pocketMonList[i+1] = poName
    pocketMonList[poName] = i+1


for i in range(1, targetNum+1):
    quizName = sys.stdin.readline().strip()
    anslist.append(quizName)


for ans in anslist:
    if ans.isdigit():
        keyNum = int(ans)
        print(pocketMonList[keyNum])
    else:
        print(pocketMonList[ans])       

pocketMonList.append

        
