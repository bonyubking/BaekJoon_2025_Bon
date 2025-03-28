T = int(input())
lst = []
quarter = 25
dime = 10
nickel = 5
penny = 1

for i in range(T):
    lst.append(list(map(int,input().split()))) 

for i in range(T):    
    for key in lst[i]:
        Anslist = []
        Anslist.append(key//quarter)
        key = key%quarter
        Anslist.append(key//dime)
        key = key%dime
        Anslist.append(key//nickel)
        key = key%nickel
        Anslist.append(key)
        print(*Anslist)
        


