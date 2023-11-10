import sys

n = int(sys.stdin.readline())
case = [[0, 0]]

for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    case.append(a)

dp = [[0] * (n + 1) for _ in range(n + 1)]

def row_and_col_multi(dp, n):
    for d in range(1, n + 1):
        for start in range(1, n + 1 - d):
            end = start + d
            result = []
            dp[start][end] = 2 ** 31
            for k in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k + 1][end] + case[start][0] * case[k][1] * case[end][1])
    return dp[start][end]

a = row_and_col_multi(dp, n)
print(a)

               
