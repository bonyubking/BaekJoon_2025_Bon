from collections import deque

N = int(input())

jelly = []
target = []

ans = 0

for _ in range (N):
    lst = list(map(int,input().split()))
    jelly.append(lst)
        
q = deque([(0,0)])
    
while q:
    x, y = q.popleft()
    
    if x == N-1 and y == N-1:
        ans = 1
        break;
    
    temp = jelly[x][y]
    
    if temp == 0:
        continue 
      
    dx = [temp, 0]
    dy = [0, temp]
    
    for j in range(2):
        nx = x+dx[j]
        ny = y+dy[j]
        if 0 <= nx < N and 0 <= ny < N:
            q.append([nx,ny])


if ans:
    print('HaruHaru')
else:
    print('Hing')