numbers = []
max = 0
col = 1
row = 1

for i in range (9):
    numbers.append(list(map(int,input().split())))
    

for i in range(9):
    for j in range(9):
        if numbers[i][j] > max:
            max = numbers[i][j]
            col = i+1;
            row = j+1;    
    
print(max)
print(col, row) 
