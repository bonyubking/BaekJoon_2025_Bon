# 팩토리얼의 합으로 나타낼수 있느냐......

# 팩토리얼이란 -- > 1*2*3*4*5

#                  1*2
                 
def factorial(a):
    key = 1
    for i in range(1,a+1):
        key = key * i
        
    return key



fac_list = [factorial(i) for i in range(21)]

key_num = int(input())
key = key_num

for j in range(20, -1, -1):
    if key_num >= fac_list[j]:
        key_num -= fac_list[j]

if key_num == 0 and key!= 0:
    print('YES')
    
else:
    print('NO')
    



