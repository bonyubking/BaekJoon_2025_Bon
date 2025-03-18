# input -> 영단어 (대소문자)

# input 대문자로 만듬

# 알파벳 갯수 길이로 된 리스트 M 생성

# input 순회하면서 해당하는 위치에 대응되는 리스트 M 값 1올림

# 리스트 M에서 Max값 위치 찾아서 출력

Key = input()
Big = Key.upper()

cnt = [0]*26

for char in Big:
    num = ord(char)-65
    cnt[num]+= 1
    
Num = 0;

for i in range (25):
    if cnt[i] > Num:
        Num = cnt[i]

if cnt.count(max(cnt)) >=2:
    print("?")

else:
    
    a = cnt.index(max(cnt))
    print(chr(a+65))


        
        
        



