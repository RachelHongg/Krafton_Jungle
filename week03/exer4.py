import sys

T = int(sys.stdin.readline())

def deci(case):
    cnt = 0
    max_i = case[0][0]
    max_j = case[0][1]
    
    for i, j in case:
        if max_i <= i and max_j <= j:
            continue
        if j <= max_j:
            cnt += 1
    return cnt
                
for _ in range(T):
    case = []
    n = int(sys.stdin.readline())

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        case.append([a, b])
    
    case.sort(key = lambda x: x[0])
    
    a = deci(case)
    print(a)
