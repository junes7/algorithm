import sys
input=lambda:sys.stdin.readline().rstrip()
n,rlt=int(input()),0
a=[*map(int,input().split())]
b=[*map(int,input().split())]
for i in range(n):
    rlt+=abs(a[i]-b[i])
print(rlt//2)