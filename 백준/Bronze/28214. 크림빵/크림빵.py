import sys
input=lambda:sys.stdin.readline().rstrip()
n,k,p=map(int,input().split())
arr,rlt=[*map(int,input().split())],0
for i in range(n):
    cnt=0
    for j in range(k*i,k*(i+1)):
        if arr[j]==0:
            cnt+=1
    if cnt<p:
        rlt+=1
print(rlt)