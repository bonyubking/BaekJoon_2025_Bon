N = int(input())

chuu = list(map(int,input().split()))

chuu.sort()
target = 1
for num in chuu:
    if num > target: 
        break
    target += num
    
print(target)
    



