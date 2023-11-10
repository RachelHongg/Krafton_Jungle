import sys

T = int(sys.stdin.readline())
breaker = False
res = []


for _ in range(T):
    node, edge = map(int, sys.stdin.readline().split())
    result = [0] * (node + 1)
    breaker = False
    for i in range(edge):
        s, e = map(int, sys.stdin.readline().split())
        if result[s] == 0:
            if result[e] == 0:
                result[s] = 1 
                result[e] = 2
            elif result[e] == 1:
                result[s] = 2
            elif result[e] == 2:
                result[s] = 1
        elif result[s] == 1 and result[e] == 0:
            result[e] = 2
        elif result[s] == 2 and result[e] == 0:
            result[e] = 1
        else:
            breaker = True
            break
    if breaker == True :
        res.append("NO")
    else: 
        res.append("YES")

for i in range(T):
    print(res[i])