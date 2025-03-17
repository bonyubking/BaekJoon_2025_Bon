def getDigit(key):
    num1 = (key // 100)
    num2 = (key - (num1 * 100)) // 10 
    num3 = key - (num1 * 100) - (num2 * 10)
    
    return num1, num2, num3   


def countnum(totalNum):
    ans = 0
    for i in range(1, totalNum+1):
        hundredDigit, tenDigit, oneDigit = getDigit(i) 
        if (hundredDigit - tenDigit) == (tenDigit - oneDigit):
            ans = ans + 1
        elif (hundredDigit == 0):
            ans = ans + 1
        elif (hundredDigit == 0 and tenDigit == 0):
            ans = ans + 1 
    return ans


keyNum = int(input())

ansNum = countnum(keyNum)
print(ansNum)

       

