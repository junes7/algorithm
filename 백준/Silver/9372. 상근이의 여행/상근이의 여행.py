from collections import deque
def dfs(graph, v, visited,ans):	#dfs
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            ans = dfs(graph, i, visited,ans+1)
    return ans
t = int(input())
for l in range(t):
    n,m = map(int,input().split())
    graph = [[]for _ in range(n)]
    visited = [False]*n
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    print(dfs(graph,0,visited,0))