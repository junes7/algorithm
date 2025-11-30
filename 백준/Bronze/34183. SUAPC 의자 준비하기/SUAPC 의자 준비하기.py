import sys
input=lambda:sys.stdin.readline().rstrip()
n,m,a,b=map(int,input().split())
rlt=n*3-m
print(a*rlt+b if rlt>0 else 0)