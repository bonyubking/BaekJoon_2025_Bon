Key = input()
cnt = 0
i = 0

while i < len(Key):
    if Key[i] == 'c':
        if i + 1 < len(Key) and (Key[i+1] == '=' or Key[i+1] ==  '-'):
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1
    elif Key[i] == 'd':
        if i + 1 < len(Key) and Key[i+1] == '-':
            cnt += 1
            i += 2
        elif i + 2 < len(Key) and Key[i+1] == 'z' and Key[i+2] == '=':
            cnt += 1
            i += 3
        else:
            cnt += 1
            i += 1            
    elif Key[i] == 'l':
        if i + 1 < len(Key) and Key[i+1] =='j':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1            
    elif Key[i] == 'n':
        if i + 1 < len(Key) and Key[i+1] =='j':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1            
    elif Key[i] == 's':
        if i + 1 < len(Key) and Key[i+1] =='=':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1                                  
    elif Key[i] == 'z':
        if i + 1 < len(Key) and Key[i+1] =='=':
            cnt += 1
            i += 2
        else:
            cnt += 1
            i += 1                               
    else:
        cnt+=1
        i+=1

print(cnt) 