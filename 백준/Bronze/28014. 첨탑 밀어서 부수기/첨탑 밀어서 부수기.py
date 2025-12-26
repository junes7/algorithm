import sys
input=lambda:sys.stdin.readline().rstrip()
n,rlt=int(input()),1
h=[*map(int,input().split())]
for i in range(n-1):
    if h[i]<=h[i+1]:
        rlt+=1
print(rlt)