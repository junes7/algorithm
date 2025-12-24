import sys
input=lambda:sys.stdin.readline().rstrip()
a,t=map(int,input().split())
rlt=10+2*(25-a+t)
print(0 if rlt<0 else rlt)