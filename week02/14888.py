import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
max_result = - 1e9
min_result = 1e9

def dfs(depth, plus, minus, multi, divide, res):
    global total, max_result, min_result
    if depth == n:
        max_result = max(max_result, res)
        min_result = min(min_result, res)
        return max_result, min_result
    if plus:
        dfs(depth + 1, plus - 1, minus, multi, divide, res + num[depth])
    if minus:
        dfs(depth + 1, plus, minus - 1, multi, divide, res - num[depth])
    if multi:
        dfs(depth + 1, plus, minus, multi - 1, divide, res * num[depth])  
    if divide:
        dfs(depth + 1, plus, minus, multi, divide - 1, int(res / num[depth]))
    
dfs(1, op[0], op[1], op[2], op[3], num[0])        

print(max_result)
print(min_result)