N = int(input())

numlst = list(map(int,input().split()))

M = int(input())

tarlst = list(map(int,input().split()))

counts = {}

for key in numlst:
    if key in counts:
        counts[key] += 1
    else:
        counts[key] = 1
        

for key2 in tarlst:
    if key2 not in counts:
        print('0', end =' ')
    else:
        print(counts[key2], end=' ')