SwitchNum = int(input())
Switchlist = list(map(int, input().split()))
StudentNum = int(input())
Actlist = []

for i in range(0, StudentNum):
    Input = list(map(int, input().split()))
    Actlist.append(Input)

for i in range(0, StudentNum):
    if Actlist[i][0] == 1:
        Key = Actlist[i][1]
        Mok = SwitchNum // Key
        for j in range(1, Mok+1):
            Switchlist[(j*Key)-1] = 1 - Switchlist[(j*Key)-1]

    if Actlist[i][0] == 2:
        Key = Actlist[i][1]
        leftIndex = Key - 1
        rightIndex = Key - 1

        while Switchlist[leftIndex] == Switchlist[rightIndex]:
            Switchlist[leftIndex] = 1 - Switchlist[leftIndex]
            Switchlist[rightIndex] = 1 - Switchlist[rightIndex]

            leftIndex = leftIndex - 1
            rightIndex = rightIndex + 1

            if leftIndex == -1:
                break;

            elif rightIndex == SwitchNum:
                break;

        Switchlist[Key-1] = 1 - Switchlist[Key-1]

for i in range(0, SwitchNum, 20):
    chunk = Switchlist[i:i+20]
    print(*chunk)
        


           
           
      


        

        
