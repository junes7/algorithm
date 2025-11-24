import sys
input=lambda:sys.stdin.readline().rstrip()
s,n,m=map(int, input().split())
cnt=0
for i in range(n+m):
    num=int(input())
    if num==1:
        if s==cnt:
            s+=s
        cnt+=1
    else:
        cnt-=1
print(s)