N = int(input())
lst = []
i = 2
while N>1:
    

    if N % i == 0:
        lst.append(i)
        N = N//i
        i = 2
    else:
        i += 1


newlst = sorted(lst)

for i in range(len(newlst)):
    print(newlst[i])