import sys

n, amount = map(int, sys.stdin.readline().split())
coins = []
cnt = 0


for _ in range(n):
    a = int(input())
    coins.append(a)
    coins.sort(reverse = True)

for coin in coins:
    while amount - coin >= 0:
        amount = amount - coin
        cnt += 1            

print(cnt)