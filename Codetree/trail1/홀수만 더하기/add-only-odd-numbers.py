n,rlt=int(input()),0
for _ in range(n):
    elem=int(input())
    if elem%2==1 and elem%3==0:
        rlt+=elem
print(rlt)