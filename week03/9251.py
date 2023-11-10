import sys

str1 = list(sys.stdin.readline().strip())
str2 = list(sys.stdin.readline().strip())

m, n = len(str1), len(str2)
graph = [[0] * (n + 1) for _ in range(m + 1)]

def check(str1, str2, graph):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 같을 때
            if str1[i - 1] == str2[j - 1]:
                graph[i][j] = graph[i - 1][j - 1] + 1 
        
            # 다를 때
            else:
                graph[i][j] = max(graph[i - 1][j], graph[i][j - 1])
    return graph[m][n]

a = check(str1, str2, graph)
print(a)
