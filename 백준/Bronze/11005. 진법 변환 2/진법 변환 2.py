NUM, KEY = map(int, input().split())

arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = []

i = 1
while NUM > 0:
    ans.append(arr[NUM%KEY])  
    NUM = NUM // KEY  
    i += 1
    
print("".join(ans[::-1]))