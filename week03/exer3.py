N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(1 << N)]
def tsp(mask, pos):
    if mask == (1 << N) - 1:
        return W[pos][0] or float('inf')
    if dp[mask][pos] != -1:
        return dp[mask][pos]
    cost = float('inf')
    for nx in range(N):
        if mask & (1 << nx) or W[pos][nx] == 0:
            continue
        cost = min(cost, W[pos][nx] + tsp(mask | (1 << nx), nx))
    dp[mask][pos] = cost
    print("========================")
    print(mask)
    print(dp)
    print("========================")
    return cost
print(tsp(1, 0))






