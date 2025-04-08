N = int(input())
lst = []

for i in range (N):
    lst.append(int(input()))


newlst = sorted(lst)

for i in range(len(newlst)):
    print(newlst[i]) 