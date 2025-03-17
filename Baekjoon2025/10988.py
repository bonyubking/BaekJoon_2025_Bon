T = input()
cnt = 1

for i in range(len(T)-1):
    if T[i] != T[len(T)-1-i]:
       cnt = 0 
        
 

print(cnt) 
