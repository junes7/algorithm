import sys,math
input=lambda:sys.stdin.readline().rstrip()
a,b=map(int,input().split())
rlt=int(math.sqrt(a*a-b))
if rlt>0:
    print(-a-rlt,-a+rlt)
else:
    print(-a)