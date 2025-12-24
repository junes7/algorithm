import sys
input=lambda:sys.stdin.readline().rstrip()
n,rlt,bn=int(input()),0,0
grade={'A':4,'B':3,'C':2,'D':1,'E':0}
for _ in range(n):
    st=input()
    rlt+=grade.get(st[0])
    if st[0] in "ABC":
        if st[1]=='1':
            bn+=0.05
        elif st[1]=='2':
            bn+=0.025
print(rlt/n+bn)