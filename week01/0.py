
T = int(input())
nums = map(int, input().split())
deci = 0

for num in nums:
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
    if cnt == 0:
        deci += 1

print(deci)
    
    