import sys

n, k = map(int, sys.stdin.readline().split())
idx = 0
list = [i for i in range(1, n + 1)]
result = []

while list:
    idx += (k - 1)
    if idx >= len(list):
        idx %= len(list)
    result.append(list.pop(idx))
    
print("<", ", " .join(map(str,result)), ">")