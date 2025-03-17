N = int(input())
new_dict = [0,0,1,1]


for i in range(4, N+1):
    if i % 3 == 0 and i % 2 == 0:
        A = min(new_dict[i//3],new_dict[i//2],new_dict[i-1])+1
        new_dict.append(A)
    
    elif i % 2 == 0:
        A = min(new_dict[i//2], new_dict[i-1])+1
        new_dict.append(A)
        
    elif i % 3 == 0:
        A = min(new_dict[i//3], new_dict[i-1])+1
        new_dict.append(A)
        
    else:
        A = new_dict[i-1]+1
        new_dict.append(A)
          

print(new_dict[N])



