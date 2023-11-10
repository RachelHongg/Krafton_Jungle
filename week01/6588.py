import math
import sys

# 소수 판별 함수
def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        n % i == 0
        return False
    return True

T = int(sys.stdin.readline())

for i in range(T):
    num = int(sys.stdin.readline())
    
    A = num//2
    B = num//2
    
for _ in range(num//2):
    if prime(A) and prime(B):
        print(A, B)
        break
    else:
        A -= 1
        B += 1

