def solution(n, results):
    rlt = 0
    INF = 1e9
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for result in results:
        x, y = result 
        graph[y][x] = 1 
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0          
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])       
    for a in range(1, n + 1):
        count = 0
        for b in range(1, n + 1):
            if graph[a][b] != INF or graph[b][a] != INF:
                count += 1 
        if count == n:
            rlt += 1
    return rlt