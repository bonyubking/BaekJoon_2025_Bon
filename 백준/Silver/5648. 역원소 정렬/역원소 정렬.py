N, *lst = input().split()

while int(N) > len(lst):
    
    key = input().split()
    lst+= key
    

anslst =[]
for key in lst:
    anslst.append(int(key[::-1]))
    
anslst.sort()
    
for i in anslst:
    print(i)