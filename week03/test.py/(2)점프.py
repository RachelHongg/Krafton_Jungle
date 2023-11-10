import sys

# 입력 받기
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
print(graph)            # test

# dfs로 풀기(탑다운)
def dfs(i, j, dp):
    if i == N - 1 & j == N - 1:         # 종료조건
        return dp[i][j] 
    # 이동 거리 넣기
    move = graph[i][j]
    # 오른쪽으로 이동
    if i + move < (N - 1):
        a = dp[i][j + move] + dfs(i, j + move)
    else: a = 10**6
    # 아래로 이동
    if j + move < (N - 1):
        b = dp[i + move][j] + dfs(i + move, j)
    else: b = 10**6    
    
    minimum = min(a, b)
    dp[i][j] = minimum
    return i, j, dp
# dp 테이블 만들어, 현재 위치가 종착점일때 최솟값 저장하기

dfs(0, 0, dp)
print(dp[N - 1][N - 1])