import sys
cnt_x = 0
cnt_y = 0
cnt_x_link = 0
cnt_y_link = 0

row, col = map(int, sys.stdin.readline().split())
graph = [] * (row)

for _ in range(row):
    graph.append(list(map(str, sys.stdin.readline().strip())))

# 한 행씩 탐색
for j in range(row):
    for i in range(col):
        if graph[j][i] == '-':
            cnt_x += 1
            if i < col - 1 and graph[i][j + 1] == '-':
                cnt_x_link += 1

# 한 열씩 탐색
for i in range(col):
    for j in range(row):
        if graph[i][j] == '|':
            cnt_y += 1
            if i < row - 1 and graph[i + 1][j] == '|':
                cnt_y_link += 1
                
cnt_total = (cnt_x - cnt_x_link) + (cnt_y - cnt_y_link)
print(cnt_x, cnt_x_link, cnt_y, cnt_y_link)
print(cnt_total)