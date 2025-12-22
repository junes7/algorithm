import sys
input=lambda:sys.stdin.readline().rstrip()
n,m=map(int,input().split())
arr=[]
for i in range(1,n+1):
    arr.append([j for j in range((i-1)*m+1,i*m+1)])
for i in range(n):
    print(*arr[i])