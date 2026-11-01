def solution(tickets):
    rlt = []
    visited = [False] * len(tickets)
    def dfs(start, path): 
        if (len(path) == len(tickets) + 1):
            rlt.append(path)
            return
        for idx, ticket in enumerate(tickets):
            if (ticket[0] == start) and (not visited[idx]):
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False     
    dfs("ICN", ["ICN"])
    rlt.sort()
    return rlt[0]