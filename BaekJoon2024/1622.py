import sys

try :
    while True:
        keyWord3 = []
        keyWord1 = input()
        keyWord2 = input()
        
        for key in keyWord1:
            if key in keyWord2:
                    keyWord2 = keyWord2.replace(key,'',1)
                    keyWord3 += [key]
        
        keyWord3.sort()
        print(''.join(keyWord3))
            
except :
    pass
            




### ''.join(A) 로 문자열 합칠수 잇음
####    .replace(key,'',1) 문자열 대체하는 함수
###sys.stdin.readline().strip()
