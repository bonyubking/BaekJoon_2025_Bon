inputlist = list(map(int, input().split()))


X = inputlist[0]
Y = inputlist[1]
W = inputlist[2]
S = inputlist[3]



if S > (2*W):
    ans = (X+Y)*W

elif S < W:
    if (X+Y) % 2 == 1:
        ans = (max(X,Y)-1)*S + W 
    else:
        ans = (max(X,Y))*S

else:
    ans = min(X,Y)* S + (max(X,Y) -min(X,Y))* W
    

print(ans)        