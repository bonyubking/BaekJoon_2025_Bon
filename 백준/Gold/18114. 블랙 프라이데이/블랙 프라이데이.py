N,C = map(int,input().split())

price = list(map(int,input().split()))

price.append(0)
price.append(0)
price.sort()


for i in range(N+2): 
    
    l = 0 
    r = N+1
    
    while l < r:
        
        if l == i:
            l+=1
            continue
        elif r == i:
            r-=1
            continue
        elif l>=r:
            break
        
        s = price[i] + price[l] + price[r]
        
        if s == C:
            print(1)
            exit()
        elif s < C:
            l += 1
        else:
            r -= 1

print(0)