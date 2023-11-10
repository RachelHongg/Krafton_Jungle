import sys
sys.setrecursionlimit(10**6)

T =int(sys.stdin.readline())

# dfs 정의하기
def dfs(graph, v, visited, group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:                     # 아직 방문하지 않았다면,
            result = dfs(graph, i, visited, -group)
            if result == False:
                return False
        elif visited[v] == visited[i]:        # 방문했는데, 인접노드끼지 같은 그룹이라면,
                return False
    return True

# tree에 값 넣기
for _ in range(T):
    node, edge = map(int, sys.stdin.readline().split())
    tree = [[] for _ in range(node + 1)]
    
    for i in range(edge):
        s, e = map(int, sys.stdin.readline().split())
        tree[e].append(s)
        tree[s].append(e)
        
    visited = [0] * (node + 1)
    
    a = dfs(tree, 1, visited, 1)
    
    if a == True:
        print("YES")
    else:
        print("NO")
    