import sys
input=lambda:sys.stdin.readline().rstrip()
n,m=map(int,input().split())
print(n//m+(0 if n%m==0 else 1))