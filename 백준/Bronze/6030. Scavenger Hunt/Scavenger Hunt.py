import sys
input=lambda:sys.stdin.readline().rstrip("\n")
p,q=map(int,input().split())
pe=[i for i in range(1,p+1) if p%i==0]
qe=[i for i in range(1,q+1) if q%i==0]
for c in pe:
    for d in qe:
        print(c,d)