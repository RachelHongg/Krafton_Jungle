import sys

num = int(sys.stdin.readline())
result = [0] * (num + 1)

def fibo(n):
    if n ==1 or n ==2:
        return 1
    if result[n] != 0:
        return result[n]
    result[n] = fibo(n - 1) + fibo(n - 2)
    return result[n]

print(fibo(num))
    