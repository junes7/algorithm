n=int(input())
for _ in range(n):
    mul=1
    a,b=map(int,input().split())
    for i in range(a,b+1):
        mul*=i
    print(mul)