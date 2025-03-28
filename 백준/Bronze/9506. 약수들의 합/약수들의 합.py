## 완전수 - > 자신을 제외한 약수의 합과 같으면 완전수
while True:
    N = int(input())
    if N == -1:
        break;
    
    lst = []
    for i in range (1,N//2+1):
        if N%i == 0:
            lst.append(i)
            
    if sum(lst) == N:
        print(N, "=", ' + '.join(map(str, lst)))
    else:
        print(N, "is NOT perfect.");