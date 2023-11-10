import sys

T = int(sys.stdin.readline())

arr = [sys.stdin.readline().strip() for _ in range(T)]
array = sorted(set(arr))
array.sort(key=len)

for i in array:
    print(i)