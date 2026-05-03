def solution(info, n, m):
    MAX = 120 
    dp = [[False] * MAX for _ in range(MAX)]
    dp[0][0] = True 
    item_count = len(info)
    for traceA, traceB in info:
        next_dp = [[False] * MAX for _ in range(MAX)]
        for a in range(n):  
            for b in range(m): 
                if not dp[a][b]:
                    continue
                if a + traceA < n:
                    next_dp[a + traceA][b] = True
                if b + traceB < m:
                    next_dp[a][b + traceB] = True
        dp = [row[:] for row in next_dp]
    for a in range(n):
        for b in range(m):
            if dp[a][b]: 
                return a
    return -1