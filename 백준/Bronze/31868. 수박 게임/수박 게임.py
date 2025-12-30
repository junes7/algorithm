import sys
input=lambda:sys.stdin.readline().rstrip()
n,k=map(int,input().split())
for i in range(n-1):
    k//=2
print(k)