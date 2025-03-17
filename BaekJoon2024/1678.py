T, M, N = map(int,input().split())
train_dic = {}
ans = 0
que = 0

for i in range(T):
    train_info = input().split()
    train_num = train_info[0]
    train_times = list(map(int, train_info[1:-1]))
    train_dic[train_num] = train_times


time_list = sum(train_dic.values(),[])
time_list.sort()

current_time = M

N = N % len(time_list)

mynum = None

for i in range(len(time_list)):
    if M <= time_list[i]:
        que = i
        
ans = (que+N)%(len(time_list))


for key, value in train_dic.items():
    if time_list[ans] in value:
        mynum = key

        
    

print(mynum)
