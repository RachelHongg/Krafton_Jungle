import sys

node, edge = [int(sys.stdin.readline()) for _ in range(2)]
tree = [[] for i in range(node + 1)]
visited = [False] * (node + 1)
cnt = 0

for _ in range(1, edge + 1):
    start_edge, end_edge = map(int, sys.stdin.readline().split())
    tree[start_edge].append(end_edge)
    tree[end_edge].append(start_edge)

def dfs(graph, v):
    global visited, cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i)
            cnt += 1
    return cnt

print(dfs(tree, 1))