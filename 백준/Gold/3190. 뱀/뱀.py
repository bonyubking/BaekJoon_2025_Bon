## N*N 이고 뱀의 머리위치가 (m, -1) (-1, m) (N, m) (m, N) 이면 종료
## 사과를 만나면 꼬리 위치는 그대로고 머리 위치만 +1 
## 사과 없으면 꼬리 위치 +1 머리위치 +1
## 기존은 1초마다 (1,0) 이동 하고 X초에 D면 (0, -1) C면 (0, 1)
## 기존 움직임이 (a, 0) 이면 D만나면 (0, -a) C만나면 (0, a) 이동ㅎ으로바낌

from collections import deque

N = int(input())
K = int(input())
apple = []
for _ in range (K):
    a, b = map(int,input().split())
    apple.append([a-1,b-1])

turn = [0] * 10001
L = int(input())
for _ in range (L):
    c, d = input().split()
    turn[int(c)] = d

x, y = 0, 0
direction = [0,1]
snake = deque()
snake.append([0,0])
key = 0
time = 0

while True:
    
    time += 1
    
    ## 1번 조건
    nx = x + direction[0]
    ny = y + direction[1]        
    
    ## 2번 조건
    if 0 > nx or nx >= N or 0 > ny or ny >= N:
        break
    
    ## 2번 조건 2
    if [nx, ny] in snake:
        break
    
    snake.append([nx,ny])
         
    ## 3번 조건     
    if [nx, ny] in apple:
        apple.remove([nx, ny])
    ## 4번 조건
    else:
        snake.popleft()  
    
    if turn[time] == 'D':      
        dx, dy = direction
        direction[0], direction[1] = dy, -dx

    elif turn[time] == 'L':   
        dx, dy = direction
        direction[0], direction[1] = -dy, dx
        
    x, y = nx, ny

          
print(time)