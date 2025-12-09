## 그냥 sort 했을때 문제점은 맨뒤랑 맨앞이 간극이너무커진다
## 젤작은걸 맨앞 그담거 맨뒤 그담 맨앞에서2 그다음 맨뒤에서2 이런식이 맞는거같다

T = int(input())

for _ in range (T):
    
    cnt = int(input())
    trees = list(map(int,input().split()))
    trees.sort()
    ans = 0
    
    for i in range (cnt-2):
        ans = max(ans, trees[i+2]-trees[i])
    
    print(ans)