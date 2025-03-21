words = []
result = ""

for i in range (5):
    words.append(list(input()))


for j in range(15):  
    for i in range(5):  
        if j < len(words[i]):  
            result += words[i][j]
            
print(result)