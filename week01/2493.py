# range를 반대로 돌릴 때는 인덱스에 조심하자.

# #이중 for문 이용한
# import sys

# n = int(sys.stdin.readline())
# tops = list(map(int, sys.stdin.readline().split()))
# result = [0] * n

# for std in range(n , 0, -1):
#     for bro in range(n , 0, -1):
#         if std > bro and tops[bro - 1] > tops[std - 1]:
#             result[std - 1] = bro
#             break

# result.reverse()
# print(result)

# 스택 구조 이용한
n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0 for i in range(n)]
 
for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])
 
print(*answer)




