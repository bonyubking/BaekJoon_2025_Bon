keyWord = input()
targetWord = input()


for i in range(0,len(keyWord)-len(targetWord)):
    if keyWord[i : i+len(targetWord)] == targetWord:
        count = count + 1
        i = i + len(targetWord)

print(count)
            
            
            
            
            
