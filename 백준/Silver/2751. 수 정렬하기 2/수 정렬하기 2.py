import sys

N = int(sys.stdin.readline())
numlst = []

for i in range (N):
    numlst.append(int(sys.stdin.readline()))
    
numlst.sort()

for i in numlst:
    print(i)
