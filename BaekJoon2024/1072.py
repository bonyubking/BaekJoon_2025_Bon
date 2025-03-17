import math



X, Y  = map(int,input().split())


 
win_Rate = math.floor(Y*100/X)
start = 1
end = 1000000000+X
if win_Rate >= 99:
    print('-1')
    exit()
    
while start <= end:
    key = (start+end)//2
    new_win_Rate = math.floor((Y+key)/(X+key)*100)
    if new_win_Rate - 1 >= win_Rate:
        end = key-1
    else:
        start = key+1       



print(start)





   
    
    


