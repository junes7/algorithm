def solution(n, count):    
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n):
        for j in range(1, i+1):
            dp[i+1][j+1] += dp[i][j] % 1000000007
            dp[i+1][j] += dp[i][j]*2*i % 1000000007
    return dp[n][count] % 1000000007