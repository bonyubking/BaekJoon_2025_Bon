T = int(input())
for i in range(T):
    num, text = input().split()
    num = int(num)

    ans = ""
    for key in text:
        ans+= key * num
        
        
    print(ans)
