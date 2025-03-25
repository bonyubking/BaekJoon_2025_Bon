A, B, V = map(int,input().split()) 





key = V-A

ans = key//(A-B)


if key%(A-B) != 0:
   ans = ans + 2
else:
    ans = ans + 1 

        
print(ans)
