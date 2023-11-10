N = int(input())
nums = map(int, input().split())
deci = 0

for num in nums:
    if num > 1:
        cnt = 0
        for j in range(2, num):
            if num % j == 0:
                cnt += 1
        if cnt == 0:
            deci += 1
print(deci)