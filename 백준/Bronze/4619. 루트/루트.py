import sys
input=lambda:sys.stdin.readline().rstrip()
while 1:
    b,n=map(int,input().split())
    if b==n==0: break
    a=0
    while a**n<b:
        a+=1
    print(a if a**n-b<b-(a-1)**n else a-1)