N = int(input())


lst = list(map(int,input().split()))

dic = {}

newset = sorted(set(lst))

for i in range(len(newset)):
    dic[newset[i]] = i
    
for key in lst:
    print(dic[key], end=' ')
    