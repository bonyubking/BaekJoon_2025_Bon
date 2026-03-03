T = int(input())

for _ in range (T):
    ans=0
    N = int(input())
    cycle = list(map(int,input().split()))
    visited = [0] * (N+1)
    for i in range (1, N+1):
        
        if visited[i] == 1:
            continue
        
        temp=i
        
        while True:
            temp = cycle[temp-1]
            if visited[temp] == 1:
                ans+=1
                break;
            else:
                visited[temp] = 1

    print(ans)
                     
            
            
            
            
        