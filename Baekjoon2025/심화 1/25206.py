numbers = []
for i in range(20):
    numbers.append(list(map(str,input().split())))
total = 0

column_1 = [float(row[1]) for row in numbers]
column_2 = [row[2] for row in numbers]

for i in range(len(column_2)):
    if column_2[i] == 'A+':
        column_2[i] = 4.5
    elif column_2[i] == 'A0':
        column_2[i] = 4.0
    elif column_2[i] == 'B+':
        column_2[i] = 3.5
    elif column_2[i] == 'B0':
        column_2[i] = 3.0
    elif column_2[i] == 'C+':
        column_2[i] = 2.5 
    elif column_2[i] == 'C0':
        column_2[i] = 2.0   
    elif column_2[i] == 'D+':
        column_2[i] = 1.5   
    elif column_2[i] == 'D0':
        column_2[i] = 1.0   
    elif column_2[i] == 'F':
        column_2[i] = 0.0
    elif column_2[i] == 'P':
        column_1[i] = 0.0
        column_2[i] = 0.0  
    total += column_2[i] * column_1[i]                           



print(column_1)
print(column_2)
hakjum = sum(column_1)
print(total/hakjum)

    
