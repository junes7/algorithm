import sys
input=lambda:sys.stdin.readline().rstrip()
n,m,s=map(int,input().split())
print(min(s*m,s*(m+1)*(100-n)//100))