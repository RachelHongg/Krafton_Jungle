import sys

N = int(sys.stdin.readline())

# 입력 받는 거 어떻게 하는지? 뛰어쓴게 아니라서..
for i in range(N):
    tree = list(map(int, sys.stdin.readline()))
    
def quad_tree(N, tree):
    print('(')
    # 왼쪽 위
    for i in range(0, N//2 + 1):
        for j in range(0, N//2 + 1):
            if tree[i][j] == 1:
                print(1)
            elif tree[i][j] == 0:
                print(0)
    print('(')
    # 오른쪽 위
    for i in range(0, N//2 + 1):
        for j in range(N//2 + 1, N + 1):
            if tree[i][j] == 1:
                print(1)
            elif tree[i][j] == 0:
                print(0)
    # 왼쪽 아래
    for i in range(N//2 + 1, N + 1):
        for j in range(0, N//2 + 1):
            if tree[i][j] == 1:
                print(1)
            elif tree[i][j] == 0:
                print(0)
    # 오른쪽 아래
    for i in range(N//2 + 1, N + 1):
        for j in range(N//2 + 1, N + 1):
            if tree[i][j] == 1:
                print(1)
            elif tree[i][j] == 0:
                print(0)
    # if랑 elif에 걸리지 않으면, 재귀
    quad_tree(N//2, tree)
