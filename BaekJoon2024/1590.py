busNum, manTime = map(int,input().split())
actualTimeList = []

for i in range(0, busNum):
    timeList = []
    arrival, interval, buscount = map(int, input().split())
    for j in range(0, buscount):
        waitTime = arrival + (interval*j) - manTime
        if waitTime >= 0:
            timeList.append(waitTime)
    if timeList:
        actualTimeList.append(min(timeList))

    

    
if not actualTimeList:
    print(-1)
else:    
    print(min(actualTimeList))
