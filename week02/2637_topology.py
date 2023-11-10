import sys
from collections import deque

final = int(sys.stdin.readline())
link = int(sys.stdin.readline())

graph = [[] for _ in range(final + 1)]
indegree = [0] * (final + 1)
result = []

for _ in range(link):
    a , b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    indegree[b] += 1

def topology_sort():
    global result
    queue = deque()
    
    for i in range(1, final + 1):
        if indegree[i] == 0:
            queue.append(i)
        
    while queue:
        v = queue.popleft()
        result.append(v)
        for i in graph[v]:
            indegree[i[0]] -= 1
            if indegree[i[0]]== 0:
                queue.append(i)
    return result

topology_sort()
print(result)
    
    