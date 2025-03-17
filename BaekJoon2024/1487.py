Num = int(input())
List = []
A1 = []
B1 = []
Lis = []
count = 0

def takeinput():
  
    for i in range(Num):
        Paylist = input()
        Paylist = Paylist.split(' ')
        Lis.append([int(x) for x in Paylist])
    
    return Lis;

def sorting(List):                                
    Numb = len(List)                                   
    while Numb > 1:                                 
                                                           
        for i in range(0, Numb-1):  
            if List[i][0] > List[i+1][0]:
     
                List[i][0], List[i+1][0] = List[i+1][0], List[i][0]
                
                List[i][1], List[i+1][1] = List[i+1][1], List[i][1]
 
        Numb -= 1
    
    return List;

def findanswer3(anslist):
    copylist = []
    ans2list = []
    keynumlist = []
    for i in range(0, len(anslist)):
        copylist = anslist[:]
        keynum = copylist[i][0]
        money = 0
        
        for j in range(i, len(anslist)):
            if copylist[j][1] < keynum:
                money = money + keynum - copylist[j][1] 
                keynumlist.append(keynum)
                ans2list.append(money)
    
    
    return ans2list, keynumlist

                
                
A1 = takeinput()
A11 = A1
B1 = sorting(A1)

valuelist, keynumlist = findanswer3(B1)


if valuelist == []:
    print(0)
else:
    indexNum = valuelist.index(max(valuelist))
    print(keynumlist[indexNum])

