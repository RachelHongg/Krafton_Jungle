import sys

T = int(sys.stdin.readline())
cnt = 0
result = []

for _ in range(T):
    node, edge = map(int, sys.stdin.readline().split())
    parent = [0] * (node + 1)

    for i in range(node + 1):
        parent[i] = i
    
    for i in range(edge):
        s, e = map(int, sys.stdin.readline().split())
        # union_parent 함수
        if parent[s] > parent[e]:
            parent[e] = parent[s] 
        else:
            parent[s] = parent[e]

    for i in range(2, node + 1):
        if parent[i] != parent[1]:
            cnt += 1        
    
    if cnt == 0:
        result.append("YES")
    else:
        result.append("NO")
for res in result:
    print(res)
        
    
