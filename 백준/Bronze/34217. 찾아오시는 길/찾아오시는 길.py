import sys
input=lambda:sys.stdin.readline().rstrip()
a,b=map(int,input().split())
c,d=map(int,input().split())
if (a+c)==(b+d):
    print("Either")
else:
    if (a+c)<(b+d):
        print("Hanyang Univ.")
    else:
        print("Yongdap")