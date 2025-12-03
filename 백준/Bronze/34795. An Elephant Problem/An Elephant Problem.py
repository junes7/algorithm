import sys
input=lambda:sys.stdin.readline().rstrip()
m,d=map(int,input().split())
print(d//m+(0 if d%m==0 else 1))