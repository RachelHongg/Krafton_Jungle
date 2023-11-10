import sys

T = int(sys.stdin.readline())
a = []

for _ in range(T):
    coin_num = int(sys.stdin.readline())
    coin = list(map(int,sys.stdin.readline().split()))
    coin.sort()
    amount = int(sys.stdin.readline())

    dp = [0] * (amount + 1)

    for i in range(coin_num):
        dp[0] = 1
        for j in range(coin[i], amount + 1):
            # 갱신 값 = 본래 값 + 자신의 최소 코인을 뺀 값
            dp[j] = dp[j] + dp[j - coin[i]]

    a.append(dp[amount])

for i in range(T):
    print(a[i])

        
        
        

    
