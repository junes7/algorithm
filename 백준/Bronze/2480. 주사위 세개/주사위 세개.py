import sys
input=lambda:sys.stdin.readline().rstrip()
a,b,c=map(int,input().split())
if a==b==c:
    prize=10000+a*1000
elif a==b or a==c or b==c:
    if a==b or a==c:
        prize=1000+a*100
    else:
        prize=1000+b*100
else:
    prize=max(a,b,c)*100
print(prize)