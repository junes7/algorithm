import sys,math
input=lambda:sys.stdin.readline().rstrip()
n,rlt=int(input()),0
for i in range(1,n+1):
    if n%i==0:
        rlt+=i
print(5*rlt-24)