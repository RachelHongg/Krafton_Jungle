import sys
from collections import deque

node, edge, dis, start = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)
result = []

for _ in range(edge):
    s, e = map(int, sys.stdin.readline().split())
    tree[s].append(e)

def bfs(graph, start, distance, visited):
    global result
    map = [0] * (node + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited:
                queue.append(i)
                visited = True
                map[i] = map[v] + 1
                if map[i] == distance:
                    print("-----------")
                    result.append(i)
    return result
                    

bfs(tree, start, dis, visited)
print(result)
    