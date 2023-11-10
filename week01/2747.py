# import sys

# def piv(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         result = piv(n - 1) + piv(n - 2)
#         return result

# x = int(sys.stdin.readline())

# print(piv(x))
# 시간 초과 뜸

import sys

n = int(sys.stdin.readline())

a, b = 0, 1

for i in range(n):
    a, b = b, a + b 
 
print(a)