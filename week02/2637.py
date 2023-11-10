import sys
input = sys.stdin.readline


fin_pdt = int(input())
graph = [[] for _ in range(fin_pdt + 1)]
result = [0] * (fin_pdt + 1)
multi = 1
visited = [False] * (fin_pdt + 1)
T = int(input())

for _ in range(T):
    end_pdt, start_pdt, num = map(int, input().split())
    graph[end_pdt].append([int(start_pdt), int(num)])

def dfs(graph, v, visited):
    global result, multi
    visited[v] = True
    i, j = graph[v][1]
    multi *= j
    for x, y in graph[v]:
        if len(graph[x]) == 0:
            result[x] += (y * multi)
            multi = 1
        if not visited[x]:
            dfs(graph, x, visited)
    return result

dfs(graph, fin_pdt, visited)
print(result)
    