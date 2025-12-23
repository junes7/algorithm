import sys
input=lambda:sys.stdin.readline().rstrip()
d1,d2,d3=map(int,input().split())
sumn=(d1+d2+d3)/2
a=sumn-d3
b=sumn-d2
c=sumn-d1
if a>0 and b>0 and c>0:
    print(1)
    print("%.1f %.1f %.1f" % (a,b,c))
else:
    print(-1)