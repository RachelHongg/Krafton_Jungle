import sys
n = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
dp = [1] * n
cnt = 0

for i in range(len(graph)):
    cnt = 1
    for j in range(0, i):
        if graph[j] < graph[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))