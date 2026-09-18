def solution(n):
    dp = [1,1,3,10] + [0]*(n-3)
    sp_c2, sp_c3 = 2, 5
    sp_cases = [12, 2, 4] #각각 6, 4, 5 일 때 초기에 더해지는 값들
    if n <= 3 : return dp[n]
    for idx in range(4,n+1):
        sp_c = idx%3
        total = sp_cases[sp_c]
        total += dp[idx-1] + sp_c2*dp[idx-2] + sp_c3*dp[idx-3]
        dp[idx] = total
        sp_cases[sp_c] += dp[idx-1]*2 + dp[idx-2]*2 + dp[idx-3]*4  
    rlt = dp[n]%1000000007
    return rlt