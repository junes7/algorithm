def solution(n, infection, edges, k):
    # 1. 그래프 구성 (인접 리스트)
    graph = [[] for _ in range(n + 1)]
    for x, y, pipe_type in edges:
        graph[x].append((y, pipe_type))
        graph[y].append((x, pipe_type))
    
    # 2. 확산 시뮬레이션 (BFS)
    def spread(infected, pipe_type):
        new_infected = set(infected)
        queue = list(infected)
        
        while queue:
            node = queue.pop(0)
            for neighbor, edge_type in graph[node]:
                if edge_type == pipe_type and neighbor not in new_infected:
                    new_infected.add(neighbor)
                    queue.append(neighbor)
        
        return new_infected
    
    # 3. 완전탐색 (재귀)
    def dfs(infected, remaining_k):
        if remaining_k == 0:
            return len(infected)
        
        best = len(infected)
        
        for pipe_type in [1, 2, 3]:
            new_infected = spread(infected, pipe_type)
            result = dfs(new_infected, remaining_k - 1)
            best = max(best, result)
        
        return best
    
    # 4. 실행
    return dfs({infection}, k)