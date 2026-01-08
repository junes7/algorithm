import sys
input=lambda:sys.stdin.readline().rstrip("\n")
while True:
    n=int(input())
    if n==0: break
    rlt=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            rlt+=i*j
    print(rlt)