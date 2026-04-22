import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n,data=int(input()),[*map(int,input().split())]+[0]
presum=[0]
for i in range(n):
    presum+=[presum[-1]+data[i]]
stack,rlt=[],0
for i in range(n+1):
    h,j=data[i],i
    while stack and stack[-1][0]>=h:
        h1,j=stack.pop()
        rlt=max(rlt,(presum[i]-presum[j])*h1)
    stack.append((h,j))
print(rlt)