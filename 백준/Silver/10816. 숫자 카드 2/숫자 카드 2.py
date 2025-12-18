N = int(input())

numlst = sorted(list(map(int,input().split())))

M = int(input())

tarlst = list(map(int,input().split()))

numcnt = {}

for n in numlst:
    if n in numcnt:
        numcnt[n] += 1
    else:
        numcnt[n] = 1
        
def binsearch(array, target, start, end):
    
    while end >= start:
        
        mid = (start + end) // 2
        
        if target == array[mid]:
            
            return numcnt[array[mid]]
    
        elif target < array[mid]:
            
            end = mid - 1
        
        else:
            
            start = mid + 1
            
    return 0;

for i in tarlst:
    print(binsearch(numlst, i, 0, N-1), end= ' ')
