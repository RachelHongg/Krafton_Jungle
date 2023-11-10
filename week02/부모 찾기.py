import sys

# 부모 찾기
def find_parent(parent, x):
    if parent[x] != x:
        x = parent[x]
    return x

# 부모 합치기
def union_parent(parent, a, b):
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    
    if parent_a > parent_b:
        parent[b] = parent_a
    else:
        parent[a] = parent_b

# 입력 받기
node, edge = map(int, sys.stdin.readline().split())

# 부모 노드 초기화시키기
parent = [[] for i in range(node + 1)]
cnt = 0

for i in range(1, node + 1):
    parent[i] = i

# 연결된 노드 입력 받기
for i in range(1, edge + 1):
    start_edge, end_edge = map(int, sys.stdin.readline().split())
    union_parent(parent, start_edge, end_edge)


    
# 논-사이클 처리하기


print(parent)

# for i in range(1, node + 1):
#     if parent[0] != parent[i]:
#             cnt += 1

# print(cnt)
    