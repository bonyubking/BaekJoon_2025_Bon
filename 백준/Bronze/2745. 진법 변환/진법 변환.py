N, B = input().split()
B = int(B)

ans = 0

for i in N:
    if i.isdigit():  
        ans = ans * B + int(i)
    else:  
        ans = ans * B + (ord(i) - ord('A') + 10)

print(ans)