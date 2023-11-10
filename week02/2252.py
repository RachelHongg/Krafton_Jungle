import sys
from collections import deque

num, link = map(int, sys.stdin.readline().split())
graph = [[] for i in range(num + 1)]
indegree = [0] * (num + 1)

for _ in range(link):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    indegree[end] += 1


def topology_sort():
    result = []
    queue = deque()
    
    for i in range(1, num + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        v = queue.popleft()
        result.append(v)
        for i in graph[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    return result

a = topology_sort()

for i in a:
    print(i, end= " ")