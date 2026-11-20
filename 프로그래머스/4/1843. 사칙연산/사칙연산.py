def solution(arr):
    INF = int(1e9)
    min_dp = [[INF for _ in range(len(arr)//2 + 1)] for _ in range(len(arr) //2 +1)]
    max_dp = [[-INF for _ in range(len(arr)//2 + 1)] for _ in range(len(arr) //2 +1)]
    for i in range(len(arr) //2 + 1):
        min_dp[i][i] = int(arr[i * 2])
        max_dp[i][i] = int(arr[i * 2])
    for c in range(1,len(max_dp)):
        for i in range(len(max_dp) -c):
            j = i + c
            for k in range(i,j):
                if arr[k*2 + 1] == "+":
                    max_dp[i][j] = max(max_dp[i][j],max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j],min_dp[i][k] + min_dp[k+1][j])
                elif arr[k*2 +1] =='-':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])  
    return max_dp[0][-1]