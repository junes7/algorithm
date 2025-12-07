import sys
input=lambda:sys.stdin.readline().rstrip()
n,do,gi=int(input()),0,0
if n>=1000000:
    do,gi=n*0.2,n*0.8
elif 500000<=n<1000000:
    do,gi=n*0.15,n*0.85
elif 100000<=n<500000:
    do,gi=n*0.1,n*0.9
else:
    do,gi=n*0.05,n*0.95
print(int(do),int(gi))