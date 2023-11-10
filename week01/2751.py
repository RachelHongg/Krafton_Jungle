import sys

T = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for i in range(T)]

array.sort(reverse=False)
for k in array:
    print(k)