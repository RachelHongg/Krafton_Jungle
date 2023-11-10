import sys

T = int(sys.stdin.readline())

def fun():
    for _ in range(T):
        num = int(sys.stdin.readline())
        coin = list(map(int, sys.stdin.readline().split()))
        amount = int(sys.stdin.readline())
        dp = [[0] * (amount + 1) for _ in range(len(coin) + 1)]
        
        for i in range(num):
            dp[i][0] = 1
            
        for i in range(0, num):
            for now in range(1, amount + 1):
                # 첫번째 줄
                if i == 0:
                    if now % coin[0] == 0:
                        dp[0][now] = 1
                    else:
                        dp[0][now] = 0
                    continue
                # 두번째 줄
                if now - coin[i] >= 0:
                    dp[i][now] = dp[i - 1][now] + dp[i][now - coin[i]]
        
        return dp[i][amount]

a = fun()
print(a)