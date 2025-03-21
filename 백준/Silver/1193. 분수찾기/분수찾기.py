
## 분자와 분모의 합이 N인 분수
## 2  1 
## 3  3
## 4  6
## 5  7~10
## 6  11~15
## 7  16~21

N = int(input())

max = 1
sum = 1

while True:
    
    if N <= max:
        break;
    
    sum += 1;
    max += sum;
    
sum += 1

mom = max-N+1
son = sum-mom

if sum % 2 == 0:
    print(mom,'/',son, sep='')
else:
    print(son,'/',mom, sep='')


