import sys
from collections import deque

row, col = map(int,sys.stdin.readline().split())
mark = []
cnt = 0

for _ in range(row):
    mark.append(list(map(int, sys.stdin.readline().strip())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, visited, x, y):
    map = [[0] * col for _ in range(row)]
    map[0][0] = 1
    queue = deque()
    queue.append((x, y))    
    visited[x][y] = True
    while queue:
        hx, hy = queue.popleft()
        for i in range(4):
            nx = hx + dx[i]
            ny = hy + dy[i]
            if 0 <= nx < row and 0 <= ny < col and visited[nx][ny] == False and mark[nx][ny] == 1:
                queue.append((nx, ny))
                map[nx][ny] = map[hx][hy] + 1
                visited[nx][ny] = True
    return map[row - 1][col - 1]
                
visited = [[False] * col for _ in range(row)]

a = bfs(mark, visited, 0, 0)
print(a)