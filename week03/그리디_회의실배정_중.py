import sys
n = int(sys.stdin.readline())
sche_list = []
last = 0
cnt = 0

for _ in range(n):
    start, end = map(int,sys.stdin.readline().split())
    sche_list.append([start, end])

sche_list.sort(key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
sche_list.sort(key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

for start, end in sche_list:
    if start >= last:
        cnt += 1
        last = end

print(cnt)