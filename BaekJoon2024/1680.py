import sys


CaseNum = int(sys.stdin.readline().strip())

for i in range(0, CaseNum):
    j1 = 0
    Key = 0
    ansDist = 0
    totalVolume = 0    
    Sdistlist = [] 
    Svolumelist = []

    Volume, Count = map(int,sys.stdin.readline().split())
    #print(Count)
    Volume2 = Volume
    for j in range(0, Count):
        Sdist, Svolume = map(int,sys.stdin.readline().split())
        Sdistlist.append(Sdist)
        Svolumelist.append(Svolume)


    Sum1 = sum(Svolumelist)
    for j in range(0, Count-1):
        Sdistlist[j+1] -= sum(Sdistlist[:j+1])
        
    while Key != 1:
        
        
        
        if Volume2 >= Sum1:
            ansDist = sum(Sdistlist) * 2
            Key = 1   
       

        elif Svolumelist[j1] < Volume2:  
            ansDist += Sdistlist[j1]
            Volume2 -= Svolumelist[j1]
            totalVolume += Svolumelist[j1]
            Svolumelist[j1] = 0
            j1 += 1
            
        elif Svolumelist[j1] > Volume2:
            ansDist += Sdistlist[j1]
            ansDist += sum(Sdistlist[0:j1+1])
            Volume2 = Volume
            j1 = 0
        
        elif Svolumelist[j1] == Volume2:
            ansDist += Sdistlist[j1]
            ansDist += sum(Sdistlist[0:j1+1])
            Volume2 = Volume                    
            totalVolume += Svolumelist[j1]
            Svolumelist[j1] = 0            
            j1 += 1
        
        if totalVolume == Sum1:
            Key = 1
    
    
    print(ansDist)
            
    
 

            
        

#   용량
#    3           1
# 1  2
# 1  2
# 1  1
