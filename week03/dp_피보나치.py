import sys

p = [0] * 100

def fibo(n):
    p[1] = 1
    p[2] = 1
    for i in range(3, n + 1):
        p[i] = p[i - 1] + p[i - 2]
    return p[n]

a = fibo(int(sys.stdin.readline()))
print(a)
    