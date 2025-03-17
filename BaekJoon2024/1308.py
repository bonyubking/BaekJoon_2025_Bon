def FindyearDays(year):
    year = year-1
    countyear = (year // 4) - (year // 100) + (year // 400)
    totalyear = 365 * (year-countyear) + 366 * countyear
    
    return totalyear

def FindmonthDays(month):
    
    monthlist = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    month = month-1
    monthday = 0
    for i in range (1, month+1):
        monthday = monthday + monthlist[i]        
        
    return monthday

def FindspecialmonthDays(month):
    
    monthlist = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30 ,31]
    month = month-1
    monthday = 0
    for i in range (0, month+1):
        monthday = monthday + monthlist[i]        
        
    return monthday

def Decideyear(year):
    
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 0
    else:
        return 1
    
toyear, tomonth, today = list(map(int, input().split()))
dyear, dmonth, dday = list(map(int, input().split()))

if (dyear - toyear > 1000)  or  (dyear - toyear == 1000 and dmonth > tomonth):
    print("gg")

elif (dyear - toyear > 1000)  or (dyear - toyear == 1000 and dmonth == tomonth and dday >= today):
    print("gg")
        
else:
    if Decideyear(toyear) == 0:
        totaltoyear = FindyearDays(toyear) + FindspecialmonthDays(tomonth) + today

    else:
        totaltoyear = FindyearDays(toyear) + FindmonthDays(tomonth) + today
        

    if Decideyear(dyear) == 0:
        totaldyear = FindyearDays(dyear) + FindspecialmonthDays(dmonth) + dday
        
    else:
        totaldyear = FindyearDays(dyear) + FindmonthDays(dmonth) + dday            
    
    ans = totaldyear - totaltoyear

    print("D-" + str(ans))