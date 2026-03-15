import sys
input=lambda:sys.stdin.readline().rstrip("\n")
a1,a0=map(int,input().split())
c,n0=int(input()),int(input())
if (a1*n0 + a0<=c*n0) and a1<=c:
    print(1)
else:
    print(0)