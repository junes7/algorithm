import sys
input=lambda:sys.stdin.readline().rstrip()
h1,m1=map(int,input().split(":"))
h2,m2=map(int,input().split(":"))
rlt1,rlt2=h1*60+m1,h2*60+m2
print("YES" if rlt1<rlt2 else "NO")