import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(1 << n)]

def tsp(visited, now):
    print(visited)
    if visited == (1 << n) - 1:
        print('---------')
        print(dp)
        return graph[now][0] or float('inf')
    
    if dp[visited][now] != -1:
        print('!!!!!!!!!!')
        print(dp)
        return dp[visited][now]
    
    cost = float('inf')
    for next in range(n):
        if visited & (1 << next) or graph[now][next] == 0:  # 0이 아닌 값들은 True
            continue
        cost = min(cost, graph[now][next] + tsp(visited | (1 << next), next))
    dp[visited][now] = cost
    print('+++++++++++')
    print(dp)
    return cost

print(tsp(1, 0))
print(dp)               # test