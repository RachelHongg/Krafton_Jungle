# import sys

# node, edge = map(int, sys.stdin.readline().split())
# visited = [False] * (node + 1)
# cnt = 0

# # 입력받을 tree 초기화하기
# tree = [[] for i in range(node + 1)]

# # 입력받을 visited 초기화하기
# visited = [False] * (node + 1)

# def dfs(graph, v):
#     global visited
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i)

# # 입력받기
# for _ in range(edge):
#     start_edge, end_edge = map(int, sys.stdin.readline().split())
#     tree[start_edge].append(end_edge)
#     tree[end_edge].append(start_edge)

# for i in range(node + 1):
#     tree[i].sort()

# for i in range(1, node + 1):
#     if not visited[i]:
#         dfs(tree, i)
#         cnt += 1    

# print(cnt)

import sys
input = sys.stdin.readline

fin_pdt = int(input())
graph = [[] for _ in range(fin_pdt + 1)]
result = [0] * (fin_pdt + 1)

T = int(input())

for _ in range(T):
    end_pdt, start_pdt, num = map(int, input().split())
    graph[end_pdt].append((start_pdt, num))

for i in range(1, fin_pdt + 1):
    if not graph[i]:
        continue
    queue = [(i, 1)]  # 큐에 시작 노드와 가중치를 튜플로 추가
    while queue:
        n_start_pdt, n_num = queue.pop(0)
        for i, j in graph[n_start_pdt]:
            j = n_num * j
            queue.append((i, j))
            result[i] += j
            graph[i] = []  # 노드 i의 자식 노드를 더이상 탐색하지 않음

for i in range(1, fin_pdt + 1):
    if graph[i]:
        print(i, result[i])
