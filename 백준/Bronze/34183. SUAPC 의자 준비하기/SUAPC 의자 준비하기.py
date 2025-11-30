import sys
input=lambda:sys.stdin.readline().rstrip()
n,m,a,b=map(int,input().split())
rlt=n*3-m
print(0 if rlt<=0 else a*rlt+b)