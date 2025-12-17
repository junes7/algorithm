import sys
input=lambda:sys.stdin.readline().rstrip()
x=int(input())
dp=[0]*(x+1)
for i in range(2,x+1):
    dp[i]=dp[i-1]+1
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
print(dp[x])
rlt,tmp,now=[x],dp[x]-1,x
for i in range(x,0,-1):
    if tmp>=0  and dp[i]==tmp and (i+1==now or i*2==now or i*3==now):
        now=i
        rlt+=[i]
        tmp-=1
print(*rlt)