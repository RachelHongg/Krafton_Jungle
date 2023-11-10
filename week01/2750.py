import sys

T = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for i in range(T)]

for i in range(len(array)-1, 0 , -1):
    for j in range(len(array) - 1, len(array) - i - 1, -1):
        if array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]

for k in array:
    print(k)