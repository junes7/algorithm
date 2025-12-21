import sys
input=lambda:sys.stdin.readline().rstrip()
while True:
    a,b,c,d=map(int,input().split())
    if a==b==c==d==0: break
    if a<b:
        a,b=b,a
    if c<d:
        c,d=d,c
    s,e=1,100
    while s<=e:
        mid=(s+e)//2
        ra,rb=a*mid/100,b*mid/100
        fit=0 if ra>c or rb>d else 1
        if fit:
            s=mid+1
            rlt=mid
        else:
            e=mid-1
    print(f'{rlt}%')