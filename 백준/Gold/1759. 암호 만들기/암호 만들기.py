L, C = map(int,input().split())
from itertools import combinations

password = input().split()
password.sort()

key = ['a','e','i','o','u']
visited = [0] * C
ans = []

def backtrack(start, cnt):
        
    if cnt == L:
        temp = 0
        for k in ans:
            if k in key:
                temp += 1
        if temp >= 1 and L - temp >= 2:
            print("".join(ans))
        return
    
    for i in range(start, C):
        ans.append(password[i])
        backtrack(i + 1, cnt + 1)
        ans.pop()
                        

for comb in combinations(password, L):
        temp2 = 0
        for c in comb:
            if c in key:
                temp2 += 1
    
        if temp2 >= 1 and L - temp2 >= 2:
            print("".join(comb))
                
                
        
        


