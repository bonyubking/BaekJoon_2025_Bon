## 3의 배수

X = input()

count = 0
Sep = []


while len(X) >= 2:
    Sep = list(map(int,X))
    X = str(sum(Sep))
    count += 1
 
print(count)
    
if int(X) % 3 == 0:
    print('YES')

else:
    print('NO')


    

