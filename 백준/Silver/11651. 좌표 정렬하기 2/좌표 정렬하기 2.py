N = int(input())

lst = []
for i in range (N):
    lst.append(list(map(int,input().split())))


lst.sort(key= lambda x : (x[1], x[0]))

for i in lst:
    print(i[0], i[1])