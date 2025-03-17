import sys


CaseNum = int(sys.stdin.readline().strip())

for i in range(CaseNum):
    W , N = map(int,sys.stdin.readline().split())
    W1 = W
    D = 0
    for j in range(N):    
        x_i, w_i = map(int,sys.stdin.readline().split())
        if W1 < w_i:
            D += 2*(x_i)
            W1 = W - w_i         
        elif W1 == w_i:
            D += 2*(x_i)
            W1 = W
        else:
            W1 -= w_i
    
    if W1 != W:
        D += 2*(x_i)
        
    
    print(D)


# 3 3
# 1 2
# 2 2
# 3 2

# 을 예시로 들면. 

# 첫턴 = 3보다 2가 작으므로 거리는 늘리지말고, 차 용량을 2 빼줌

#         용량 = 1. 거리 = 0.

# 두번째턴 = 스레기 2가 용량 1보다 크기 떄문에 거리는 2*2 를 더해줌(집에 있는상태)
#         용량은 쓰레기를 비우고 나서 다시와서 실은 판정.
        
#         용량 = 0, 이후에 3-2 거리 = 4
        
# 세번째턴= 스레기 2가 용량 1보다 크면. 또 집에 갓다와야함. 그리고 집에갓다와서 실은 판정

#         용량 = 1 거리 = 4 + 6

# 마지막턴( 다실고나서) = 

#         용량 = 1이므로 와서 실고집가야함 . 따라서 거리 = 4 +6 +6 = 16