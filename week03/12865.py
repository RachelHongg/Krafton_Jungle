import sys

n, k = map(int,sys.stdin.readline().split())
a = [[0, 0]]

for _ in range(n):
    w, v = list(map(int, sys.stdin.readline().split()))
    a.append([w, v])

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = a[i - 1]
    for j in range(1, k + 1):
        if j - w >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[i][j])