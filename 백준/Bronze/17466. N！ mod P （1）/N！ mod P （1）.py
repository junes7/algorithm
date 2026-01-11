import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n,p=map(int,input().split())
rlt=1
for i in range(2,n+1):
    rlt=rlt*i%p
print(rlt%p)