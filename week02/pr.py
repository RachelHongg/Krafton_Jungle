import sys
from collections import deque

node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

tree = [[] for _ in range(node + 1)]
visited = [False] * (node + 1)
cnt = 0

for _ in range(edge):
    start, end = map(int, sys.stdin.readline().split())
    tree[start].append(end)
    tree[end].append(start)

def bfs(graph, ve, visited):
    global cnt
    queue = deque([ve])
    visited[ve] = True
    while queue:
        v = queue.popleft()
        cnt += 1
        for i in graph[ve]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt
                
bfs(tree, 1, visited)
print(cnt)
    