num = int(input())
wordlist = []
cnt = 0
j = 0
b = 0
for i in range (num):
    wordlist.append(input())

for i in range(num):
    b = 0
    for j in range(len(wordlist[i])-2):
        for k in range(j+2,len(wordlist[i])):
            if wordlist[i][j] == wordlist[i][k] and wordlist[i][j] != wordlist[i][k-1]:
                b = b + 1
    
    if b == 0:
        cnt += 1

        
print(cnt)