import sys
input=lambda:sys.stdin.readline().rstrip("\n")
t = int(input())
for _ in range(t):
    n=int(input())
    koong =[0]*(n+1)
    if n ==0:
        koong[0]=1
    elif n==1:
        koong[1]=1
    elif n==2:
        koong[2]=2
    elif n==3:
        koong[3]=4
    else:
        koong[0]=1
        koong[1]=1
        koong[2]=2
        koong[3]=4
        for i in range(4,n+1):
            koong[i]=koong[i-1] + koong[i-2] + koong[i-3] +koong[i-4]
    print(koong[n])