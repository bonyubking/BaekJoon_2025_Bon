N = int(input())

tri = []

for i in range (N):
    temp = list(map(int,input().split()))
    tri.append(temp)
    


for i in range (N-2,-1,-1):
    for j in range (i+1):
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
        

print(tri[0][0])