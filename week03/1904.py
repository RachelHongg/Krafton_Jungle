import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())
case = []
cnt = 0
total = 0

# 타일의 가짓수 (1의 타일은 x개, 00타일은 y개)
x = int(N // 2)
y = N % 2
case.append([x, y])


for i in range(x + 1, 1, -1):
    x -= 1
    y += 2
    case.append([x, y])

def combin(x, y):
    global cnt
    # 종료 조건
    if x == 0 and y == 0:
        cnt += 1
        return cnt
    if x > 0:
        combin(x - 1, y)
    if y > 0:
        combin(x, y - 1)


for i, j in case:
    cnt = 0
    combin(i, j)
    total += cnt

print(total % 15746)
    
