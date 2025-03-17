numbers = list(map(int,input().split()))

chess = [1,1,2,2,2,8]

ans = []

for i in range(len(numbers)):
    ans.append(chess[i]-numbers[i])
    
print(ans)