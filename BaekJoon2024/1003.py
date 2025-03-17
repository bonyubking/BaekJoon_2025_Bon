
zero_count = [1,0]
one_count = [0,1]

N = int(input())




for j in range(N):
    key = int(input())
    zero_count = [1,0]
    one_count = [0,1]

    for i in range(2, key+1):
        zero_count.append(zero_count[i-1]+zero_count[i-2]) 
        one_count.append(one_count[i-1]+one_count[i-2])
        


    print(zero_count[key], one_count[key])

    
    
    



