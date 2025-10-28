import sys
input=lambda:sys.stdin.readline().rstrip()
N,C = map(int,input().split())
b,a = N,N
for _ in range(C):
    y,x = map(int,input().split())
    if(0<=x<=a and 0<=y<=b):
        if(x*b>y*a):
            a=x
        else:
            b=y
    else:
        pass
print(a*b)