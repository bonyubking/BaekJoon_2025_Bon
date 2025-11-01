# 크루스칼 알고리즘
# 모든 간선을 가중치 오름차순으로 정렬한다.
# 가중치가 가장 낮은 간선부터 순회하면서,
# 이 간선이 추가된다면 사이클을 발생시키는지 확인한다.
# 사이클을 발생시킨다면, continue
# 사이클을 발생시키지 않는다면 추가한다.

import sys
input = sys.stdin.readline

V, E = map(int,input().split())

node = []

for _ in range (E):
    a,b,c = map(int,input().split())
    node.append((a,b,c))

node.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

def get_parent(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축
        x = parent[x]
    return x

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b: 
        parent[b] = a
    else:
        parent[a] = b        

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, c in node:
    if not same_parent(a, b):
        union_parent(a, b)
        answer += c
        
print(answer)


    