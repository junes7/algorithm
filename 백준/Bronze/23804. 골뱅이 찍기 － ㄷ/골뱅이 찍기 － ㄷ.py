import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
for i in range(n*5):
    if i<n or i>=n*5-n:
        print('@'*(n*5))
    else:
        print('@'*n)