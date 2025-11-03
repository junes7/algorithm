import sys
input=lambda:sys.stdin.readline().rstrip()
n,m=map(int,input().split())
rlt,slist,cnt=0,[],0
for i in range(n):
    road,speed=map(int,input().split())
    for j in range(road):
        slist+=[speed];
for i in range(m):
    road,speed=map(int,input().split())
    for j in range(cnt,cnt+road):
        if speed-slist[j]>rlt:
            rlt=speed-slist[j]
    cnt+=road
print(rlt)