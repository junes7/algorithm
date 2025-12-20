import sys
input=lambda:sys.stdin.readline().rstrip()
for _ in range(int(input())):
    dp=[[1,0]]
    n=int(input())
    for i in range(n):
        dp+=[[dp[i][1],dp[i][0]+dp[i][1]]]
    print(*dp[n])