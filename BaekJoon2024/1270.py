

N = int(input())
t_dic = []

for i in range(N):
    t_dic = list(map(int,input().split()))
    t_dic2 = t_dic[1:]
    t = t_dic[0]
    counts = {}

    for num in t_dic2:
        counts[num] = counts.get(num, 0) + 1
        
    max_count = max(counts.values())

    if max_count > len(t_dic2) // 2:
        for num, count in counts.items():
            if count == max_count:
                
                print(num)
                break
    
    else:
        print('SYJKGW')
    
        