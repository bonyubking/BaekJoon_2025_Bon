N, M = map(int,input().split())

import sys

Poketmon = dict()
Queslist = []

for i in range (N):
    
    key = sys.stdin.readline().strip()
    Poketmon[str(i+1)] = key
    Poketmon[key] = i+1

    
for i in range (M):
    
    Queslist.append(sys.stdin.readline().strip())
    


for i in Queslist:
    
    print(Poketmon[i])