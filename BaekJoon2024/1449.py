N, L = map(int,input().split())


list = list(map(int,input().split()))
    
 
list.sort()    
start = list[0]
count = 1
    
for i in range(len(list)):
    if list[i] in range(start, start+L):
        continue
    
    else:
        start = list[i]
        count += 1 
        


print(count)