numbers = []
maxval = 0
col = 1
row = 1

for i in range (9):
    lst = list(map(int,input().split()))
    if max(lst) > maxval:
        col = i+1
        row = lst.index(max(lst))+1
        maxval = max(lst) 
#     numbers.append(lst)
    

# for i in range(9):
#     for j in range(9):
#         if numbers[i][j] > maxval:
#             maxval = numbers[i][j]
#             col = i+1;
#             row = j+1;    
    
print(maxval)
print(col, row) 