N = int(input())
M = int(input())

node = []

for _ in range (M):
    a,b,c = map(int,input().split())
    node.append((a,b,c))

node.sort(key=lambda x: x[2])

parent = [i for i in range(N+1)]
ans = 0

def get_parent(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def same_parent(a,b):
    return get_parent(a) == get_parent(b)

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

for a,b,c in node:
    if not same_parent(a, b):
        union_parent(a,b)
        ans += c

print(ans)

        
    