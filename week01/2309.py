import sys

array = [int(sys.stdin.readline()) for i in range(9)]
total = sum(array)
diff = sum(array) - 100

for i in range(0, 8):
    for j in range(i+1,9):
        if (array[i] + array[j] == diff):
            array[i] = array[j] = -1
            break
    if array[i] == -1:
        break
result = [x for x in array if x != -1]
result.sort()

for k in result:
    print(k)
        
