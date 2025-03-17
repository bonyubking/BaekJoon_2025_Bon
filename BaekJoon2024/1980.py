n, m, t = map(int,input().split())
coke = t
sum = 0

if t < n and t < m:
    print('0', t)
    exit()


for i in range(0, (t//n)+1):
    for j in range(0, (t//m)+1):
        time = m * j + n * i
        if t - time < coke and t - time >= 0:
            sum = i + j
            coke = t - time
        elif t - time == coke:
            if i+j > sum:
                sum = i + j
                coke = t - time


print(sum, coke)


            
 





