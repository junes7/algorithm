import sys,math
input=lambda:sys.stdin.readline().rstrip()
n,k=map(int,input().split())
l=math.ceil(n/2)
arr=[*map(int,input().split())]
rlt=[1 if c<=l else n for c in arr]
print(*rlt)