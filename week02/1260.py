import sys 
from collections import deque

# dfs 함수 구현하기
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# bfs 함수 구현하기
def bfs(graph, v, visited):
        queue = deque([v])
        visited[v] = True
        
        while queue:
            v = queue.popleft()
            print(v, end = ' ')
            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
            

# 입력 데이터를 인접리스트 방식으로 담기
node, edge, start = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(node + 1)]  # 입력받은 자료 담을 리스트

for _ in range(1, edge + 1):
    edge_start, edge_end = map(int, sys.stdin.readline().split())
    tree[edge_start].append(edge_end)
    tree[edge_end].append(edge_start)

for i in range(1, node + 1):
    tree[i].sort()
    
# dfs 에 들어갈 변수 초기 세팅
visited = [False] * (node + 1)
dfs(tree, start, visited)

print('')

visited = [False] * (node + 1)
bfs(tree, start, visited)
