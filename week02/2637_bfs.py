import sys
from collections import deque
input = sys.stdin.readline

fin_pdt = int(input())
graph = [[] for _ in range(fin_pdt + 1)]
result = [0] * (fin_pdt + 1)
res = []


T = int(input())

for _ in range(T):
    end_pdt, start_pdt, num = map(int, input().split())
    graph[end_pdt].append([int(start_pdt), int(num)])

def bfs(graph, v):
    queue = deque(graph[v])
    while queue:
        n_start_pdt, n_num = queue.popleft()
        result[n_start_pdt] += n_num
        for i, j in graph[n_start_pdt]:
            j = n_num * j
            queue.append([i, j])
    return result
            
a = bfs(graph, 7)

for i in range(1, fin_pdt + 1):
    if len(graph[i]) == 0: 
        print(i, a[i])