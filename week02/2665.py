import sys
import heapq

dx = [0, 0, +1, -1]
dy = [-1, +1, 0, 0]

n = int(sys.stdin.readline())
nx = 0
ny = 0

color = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    color.append(list(map(int, sys.stdin.readline().strip())))
 
print(color)   
        
def dijkstra(a, b, color):
    q = []
    heapq.heappush(q, (0, a, b))
    visited[a][b] = True
    while heapq:
        count, na, nb = heapq.heappop(q)
        # while문 종료조건
        for i in range(4):
            if na == (n - 1) and nb == (n - 1):
                return count
            nx = na + dx[i]
            ny = nb + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                # 흰 방
                if color[nx][ny] == 1:
                    heapq.heappush(q, (count, nx, ny))
                # 검은 방
                else:
                    heapq.heappush(q, (count + 1, nx, ny))

print(dijkstra(0, 0, color))
