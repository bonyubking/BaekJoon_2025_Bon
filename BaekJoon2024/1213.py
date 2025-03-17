Key = input()


sort_key = ''.join(sorted(Key))

set_Key = list(set(sort_key))
set_Key.sort()

cnt = 0
result = ''
mid = ''

cnt_List = [0 for i in range(len(set_Key))]


for key in sort_key:
    a = set_Key.index(key)
    cnt_List[a] += 1
    

for i in range(len(cnt_List)):
    if len(sort_key) % 2 ==1:
        if cnt_List[i] % 2 == 1:
            cnt += 1
            mid = set_Key[i]
            
        
        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()
    
    else:
        if cnt_List[i] % 2 == 1:
            cnt += 1
            
        if cnt >= 1:
            print("I'm Sorry Hansoo")
            exit()
        

            

for i in range(len(cnt_List)):
    result += set_Key[i]*(cnt_List[i]//2)
    
print(result + mid + result[::-1])




         
        

    
    
