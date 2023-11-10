import sys

T = int(sys.stdin.readline())

def deci(max_i, max_j, case, cnt):
    for i, j in case:
        if max_i <= i & max_j <= j:
            continue
        if j <= max_j:
            cnt += 1
    return cnt
                
for _ in range(T):
    case = []
    cnt = 0
    n = int(sys.stdin.readline())

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        case.append([a, b])
    print(case)         # test
    case.sort(key = lambda x: x[0])
    
    max_i = case[0][0]
    max_j = case[0][1]
    
    a = deci(max_i, max_j, case, cnt)
    print(a)
