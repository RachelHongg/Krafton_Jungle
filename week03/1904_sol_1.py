import sys

T = int(sys.stdin.readline().strip())

box = [0] * 3

def tileCnt(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    box[1] = 2
    box[2] = 1
    box[0] = box[1] + box[2]
    for i in range(3, n):
        update(i)
    return box[0]

def update(n):
    tmp = box[1]
    box[1] = box[0]
    box[2] = tmp
    # 수시로 업데이트 해줘야 메모리 초과가 안뜸.
    box[0] = (box[1] + box[2]) % 15746

print(tileCnt(T))