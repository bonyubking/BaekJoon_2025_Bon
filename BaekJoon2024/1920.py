N = input()
Nlist = list(input().split())
M = input()
Mlist = list(input().split())

MlistS = set(Mlist)
print(Mlist)

NlistS = sorted(Nlist)

for i in range(len(Mlist)):
    count = 0
    start = 0
    end = len(Nlist)-1
    while start <= end:
        mid = (start+end) // 2
        if NlistS[mid] == Mlist[i]:
            count += 1
            break
        
        elif NlistS[mid] > Mlist[i]:
            end = mid - 1
        
        else:
            start = mid + 1
    
    print(count)
    

    
    
