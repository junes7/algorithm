import sys
input=lambda:sys.stdin.readline().rstrip("\n")
for _ in range(int(input())):
    n,d=map(int,input().split())
    cnt=0
    for _ in range(n):
        v,f,c=map(int,input().split())
        if v*f/c>=d:
            cnt+=1
    print(cnt)