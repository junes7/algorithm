import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
h=[*map(int,input().split())]
rlt=1
for i in range(n-1):
    if h[i]<=h[i+1]:
        rlt+=1
print(rlt)