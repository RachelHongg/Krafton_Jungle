import sys

n, s = map(int, sys.stdin.readline().split())

list = list(map(int, sys.stdin.readline().split()))

plus = 0
minus = 0

plus_cnt = 0
minus_cnt = 0

plus_list = []
minus_list = []

cnt = 0

for i in range(n):
    if list[i] >= 0:
        plus_cnt += 1
        plus_list.append(list[i])
    else:
        minus_cnt += 1
        minus_list.append(list[i])

print(plus_list, minus_list)


    
    
    
    
# for i in range(len(plus_list)):
#     for j in range(len(minus_list)):
#         if plus_list[i] + minus_list[j] == s:
#             cnt += 1