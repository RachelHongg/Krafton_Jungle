import sys

p = [0] * 301       # 최대가 300칸이므로

# 입력받기
N = int(sys.stdin.readline())
vt = [int(sys.stdin.readline()) for _ in range(N)]         # value tree
last = False

# 처음 4칸의 최댓값 정해주기
# 마지막 칸 채워져있는지 여부 확인
def init(vt, last):
    maximum = max(vt[0]+vt[1]+vt[2], vt[0]+vt[1]+vt[3], vt[0]+vt[2]+vt[3])
    if maximum == vt[0] + vt[1] + vt[2]:
        last = False
    else: last = True
    p[4] = maximum
    return maximum, last

# 다음 2칸씩 체크하기
# 마지막 칸 채워져있는지 여부 확인
def next(last, maximum, n):
    if n + 1 < N:
        if last == True:
            maximum += vt[n + 1]
        else: 
            maximum = max(vt[0] + vt[1] + next(True, vt[n] + vt[n + 1], n + 2), vt[1] + next(False, vt[n + 1], n + 2))
        p[n] = maximum
        return maximum

# 만든 함수 실행
maximum , last = init(vt, last)
for n in range(4, N):
    next(last, maximum, n)
print(p[N - 2])

# 백준 틀림