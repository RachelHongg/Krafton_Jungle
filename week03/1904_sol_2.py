import sys

n = int(sys.stdin.readline())

box = [0] * 1000001

box[1] = 1
box[2] = 2

for i in range(3, n + 1):
    # 반복문 안에서 수시로 나눠줘야 메모리 초과 안뜸
    box[i] = (box[i - 2]+ box[i - 1]) % 15746

print(box[n])