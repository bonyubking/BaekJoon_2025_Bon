import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int,input().split())
load = [[] for _ in range (N)]

house = []
chicken = []

chic_cnt = 0

can_chicken = []
dist = []

for i in range (N):
    load[i] = list(map(int,input().split()))
    
    for j in range (N):
        if load[i][j] == 1:
            house.append([i,j])
        elif load[i][j] == 2:
            chicken.append([i,j])

     
ans = 1e9

## 치킨집이 5개인데 M이 3이야
## 치킨집별로 총거리합을구해요 6

for can_chicken in combinations(chicken, M):
    temp_ans = 0   
    for nx, ny in house:
        temp = 1e9
        for dx, dy in can_chicken:
            temp = min(temp, abs(dx-nx) + abs(dy-ny))
        temp_ans += temp
    ans = min(ans, temp_ans)
        
print(ans)