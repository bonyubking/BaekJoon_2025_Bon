def totalStr():
    count = 1
    while True:
        count2 = 0
        namelist = []
        wordlist = []
        
        totalNum = int(input())
                
        if totalNum == 0:
            break
        
        for i in range(1, totalNum+1):
            Anslist = input()
            Anslist = Anslist.split(' ')
            namelist.append(Anslist[0])
            for j in range(1, totalNum):
                wordlist.append(Anslist[j])
      
        print(f"Group {count}")
        
        for i in range(0, totalNum*(totalNum-1)):
            if wordlist[i] == "N":
                key = i // (totalNum-1)
                value = i % (totalNum)
                value2 = totalNum - value - 1 
                
                print(f'{namelist[value2]} was nasty about {namelist[key]}')
                count2 = count2 + 1
        
        if count2 == 0:
            print("Nobody was nasty")        
        
        print()
        
        count = count + 1

        
        


totalStr()





    



