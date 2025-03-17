# 문제
# N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다. 
# 이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 
# 큰 정사각형을 찾는 프로그램을 작성하시오. 이때, 정사각형은 행 또는 열에 평행해야 한다.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에 수가 주어진다.

# 출력
# 첫째 줄에 정답 정사각형의 크기를 출력한다.

N, M = map(int,input().split())
NMlist = []

for i in range(N):
    K = input()
    NList = list(map(int, str(K)))
    NMlist.append(NList)

minX = min(N,M) 
    
def findanswer(a):
    for i in range(N-a+1):
        for j in range(M-a+1):
            if NMlist[i][j] == NMlist[i][j+a-1]==NMlist[i+a-1][j]==NMlist[i+a-1][j+a-1]:
                return True
            
    return False
    

for k in range(minX, 0 , -1):
    if findanswer(k):
        print(k**2)
        break
        
    
    
    

        
