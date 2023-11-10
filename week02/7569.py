import sys

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

x, y, z = map(int, sys.stdin.readline().split())
