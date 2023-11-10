import sys
cnt_x = 0
cnt_y = 0

row, col = map(int, sys.stdin.readline().split())
graph = [] * (row)

for _ in range(row):
    graph.append(list(map(str, sys.stdin.readline().strip())))

visited = [[False] * (row) for _ in range(col)]

# 같은 행일때


# 같은 열일떄

# dfs
def dfs(graph, x, y, visited):
    global cnt_x, cnt_y 
    visited[x][y] = True
    if x == col - 1 and y == row - 1:
        return cnt_x, cnt_y
    if graph[x][y] == '-':
        if 0 <= x + 1 < col and 0 <= y < row and visited[x + 1][y] == False:
            if graph[x + 1][y] == '-':
                dfs(graph, x + 1, y, visited)
            else:
                cnt_x += 1
                dfs(graph, x + 1, y + 1, visited)
    if graph[x][y] == '|':
        if 0<= x < col and 0 <= y + 1 < row and visited[x][y + 1] == False:
            if graph[x][y + 1] == '|':
                dfs(graph, x, y + 1, visited)
            else:
                cnt_y += 1
                dfs(graph, x, y + 1, visited)

a, b = dfs(graph, 0, 0, visited)
print(a, b)


