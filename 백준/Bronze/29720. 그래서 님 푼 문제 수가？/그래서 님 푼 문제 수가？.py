import sys
input=lambda:sys.stdin.readline().rstrip()
n,m,k=map(int,input().split())
print(max(n-m*k,0),n-m*(k-1)-1)