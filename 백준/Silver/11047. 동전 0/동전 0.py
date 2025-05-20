N, K = map(int, input().split())

lst = []

for i in range(N):
    lst.append(int(input()))

lst.sort(reverse=True)

cnt = 0
 
for i in range(N):
    
      cnt += K // lst[i]
      K = K % lst[i]

        
print(cnt)   