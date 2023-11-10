import sys

def hanoi(start, end, n):
    # 종료 조건
    if n == 1:
        print(start, end)
        return 0
    hanoi(start, 6 - start - end, n - 1)
    print(start, end)
    hanoi(6 - start - end, end, n - 1)


N = int(sys.stdin.readline())
print(2**N - 1)
if(N <= 20):
    hanoi(1, 3, N)
