## 체스에서 퀸은 상하 대각 무한으로 이동가능
## (m,n) 에 있는 퀸은 (m+k, n+k), (m+k, n), (m, n+k) 로 이동가능한듯
## 두개가 이동가능하려면 x2=x1 or y1=y2 or x2-x1 = y2-y1 -> x2-y2 = x1-y1
## 잘못생각했음 행을 돌면서 어차피 가로는 다커버치니까 행당 1개 놓을수있고 열당 1개놓을수있음
## 대각은 별도로생각 (1행부터 출발하니까 위로는갈 필요없음)
## 생각못한 부분 -> 대각선으로 갈떄 일일이 2차원배열에 다체크해주려고 처음에했는데
## 2*N 길이의 1차원 배열을 선언해서
## (1,1) 에서 오른쪽아래로 갈떄 값(2,2) (3,3) (4,4) 는 다 row-col+N값이 같고
## (3,3) 왼쪽 아래로 갈떄 (2,4) (1,5) (0,6) 는 row+col 값이 같다
## 이걸 이용해서 이중포문 없이 백트랙 로직내에서 두개의 값만 1로바꿔주면 알아서 
## 대각선에 있는애들은 다 방문처리된다는걸 이용해야한디ㅏ



N = int(input())

answer= 0

col_used = [0] * N             
diag1 = [0] * (2*N)  ## 행+열값 체크를위한 공배열하나(왼쪾 아래로 이동)           
diag2 = [0] * (2*N)  ## 두번쨰 공배열 (오른쪽 아래로 이동)

def backtrack(row):
    global answer   
    if row == N:
        answer += 1
        return
    
    for i in range(N):
        if col_used[i] == 0 and diag1[row+i] == 0 and diag2[row-i+N] == 0:
        
            col_used[i] = 1
            diag1[row+i] = 1
            diag2[row-i+N] = 1
            
            backtrack(row + 1)
            
            col_used[i] = 0
            diag1[row+i] = 0
            diag2[row-i+N] = 0

backtrack(0)

print(answer)
                    
                
                    
    
