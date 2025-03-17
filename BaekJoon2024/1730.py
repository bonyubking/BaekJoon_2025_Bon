import sys

N = int(sys.stdin.readline().strip())
Keyword = sys.stdin.readline().strip()
A_list = []
B_list = []
x_i = 0


for i in range(N*N):
    A_list.append("")
    B_list.append("")

for i in range(len(Keyword)):

    if Keyword[i] == 'D':
        if x_i >= N*(N-1):
            continue
        A_list[(x_i)] += 'S'
        A_list[(x_i)+N] += 'S'
        x_i += N
    elif Keyword[i] == 'R':
        if x_i % N == N-1:
            continue
        A_list[(x_i)] += 'G'
        A_list[(x_i)+1] += 'G'
        x_i += 1
    elif Keyword[i] == 'L':
        if x_i % N == 0:
            continue
        A_list[(x_i)] += 'G'
        A_list[(x_i)-1] += 'G'        
        x_i -= 1
    elif Keyword[i] == 'U':
        if x_i < N:
            continue
        A_list[(x_i)] += 'S'
        A_list[(x_i)-N] += 'S'
        x_i -= N
    else:
        continue
    
for i in range(N*N):
    if 'G' in A_list[i] and 'S' in A_list[i]:
        A_list[i] = chr(43)
    elif 'G' in A_list[i]:
        A_list[i] = chr(45)
    elif 'S' in A_list[i]:
        A_list[i] = chr(124)
    else:
        A_list[i] = chr(46)
        
for i in range(0, len(A_list), N):
    print(''.join(A_list[i:i+N]))




    
    
    