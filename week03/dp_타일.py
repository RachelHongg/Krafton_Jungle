import sys

n = int(sys.stdin.readline())
p = [0] * 1000001

def tileCnt(n):
    p[1] = 1
    p[2] = 2
    
    for i in range(3, n + 1):
        p[i] = (p[i - 1] + p[i - 2]) % 15746
    
    return p[n]

print(tileCnt(n))