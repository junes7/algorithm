import sys
input=lambda:sys.stdin.readline().rstrip()
n,rlt,prev=int(input()),0,1000
for i in range(n):
    tmp=int(input())
    if prev>=tmp:
        prev=tmp
    else:
        rlt+=tmp-prev
print(rlt)