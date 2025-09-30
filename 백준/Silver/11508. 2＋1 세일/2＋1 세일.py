N = int(input())

milk = []
ans = 0
temp = 0

for _ in range (N):
    milk.append(int(input()))
    
milk.sort()
milk.reverse()

for key in milk:
    temp += 1
    if temp == 3:
        temp = 0
    else:
        ans += key     

print(ans)