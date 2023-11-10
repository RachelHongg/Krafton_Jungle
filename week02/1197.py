import sys

# 루트 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 갯수 n과 간선의 갯수 e를 입력받기 
n, e = map(int, sys.stdin.readline().split())

# 부모 테이블 초기화
parent = [0] * (n + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(n + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    # 비용 순으로 정렬하기 위해,튜플의 첫번째 원소를 cost로 넣는다.
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
