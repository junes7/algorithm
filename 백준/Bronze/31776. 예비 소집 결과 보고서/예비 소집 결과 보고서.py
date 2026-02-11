import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n,rlt=int(input()),0
for _ in range(n):
    arr=[*map(int,input().split())]
    if sum(arr)==-3:
        continue
    for i in range(3):
        if arr[i]==-1:
            arr[i]=121
    if arr[0]<=arr[1]<=arr[2]:
        rlt+=1
print(rlt)