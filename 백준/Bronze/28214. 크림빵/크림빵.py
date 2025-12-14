import sys
input=lambda:sys.stdin.readline().rstrip()
n,k,p=map(int,input().split())
cnt,rlt=0,0
arr=[*map(int,input().split())]
for i in range(n*k):
    if i>0 and i%k==0:
        if cnt<p:
            rlt+=1
        cnt=0
    else:
        if arr[i]==0:
            cnt+=1
if cnt<p:
    rlt+=1
print(rlt)