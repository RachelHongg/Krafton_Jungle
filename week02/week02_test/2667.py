import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [] * n
visited = [[False] * n for _ in range(n)]
cnt = 1
result = []

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# sys.setrecursionlimit(987654321)

# def dfs(graph, visited, x, y):
#     global cnt
#     if not visited[x][y] and graph[x][y] == 1:
#         for i in range(4):    
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and graph[nx][ny] == 1:
#                     cnt += 1
#                     dfs(graph, visited, nx, ny)
#     return cnt

# def bfs(graph, visited, x, y):
# segmentation fault 나옴
    
# for i in range(n):
#     for j in range(n):
#         dfs(graph, visited, i, j)
#         result.append(cnt)

print(result)



                
        