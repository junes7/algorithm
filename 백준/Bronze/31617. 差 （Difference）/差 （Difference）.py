import sys
input=lambda:sys.stdin.readline().rstrip()
k=int(input())
n=int(input())
a=[*map(int,input().split())]
m=int(input())
b=[*map(int,input().split())]
cnt=0
for i in range(n):
    for j in range(m):
        if a[i]+k==b[j]:
            cnt+=1
print(cnt)