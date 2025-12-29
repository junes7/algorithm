import sys
input=lambda:sys.stdin.readline().rstrip()
n,m=map(int,input().split())
arr=[*map(int,input().split())]
rlt=1
for c in arr:
    rlt*=c
print(rlt%m)