Num = list(map(int, input()))

List=[0,0,0,0,0,0,0,0,0,0]

for i in range(0, len(Num)):
    for j in range(0,10):
        if Num[i] == j:
            List[j] = List[j] + 1

if (List[6] + List[9]) % 2 == 0:
    List[6] = (List[6] + List[9]) // 2
    List[9] = List[6]

else:
    List[6] = ((List[6] + List[9]) // 2) + 1
    List[9] = List[6]

ans = max(List)

print(ans)
