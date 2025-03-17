vote2 = []
def candidate():
    votenum = []
    candinum = int(input())
    count = 0
    
    for i in range (candinum):
        key = int(input())
        votenum.append(key)
        
    vote1 = votenum[0]
    
    for i in range(1, candinum):
        vote2.append(votenum[i])
    
    
   
    while True:
        if vote2 == []:
            print(0)
            break;
        
        elif vote1 > max(vote2):
            print(count)
            break;
        
        else:
            vote1 = vote1 + 1
            keynum = vote2.index(max(vote2))
            vote2[keynum] = vote2[keynum] - 1
            count = count + 1    


candidate()