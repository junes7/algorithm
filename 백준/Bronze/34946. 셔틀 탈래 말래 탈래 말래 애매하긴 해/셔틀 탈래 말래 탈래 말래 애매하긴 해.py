import sys
input=lambda:sys.stdin.readline().rstrip()
a,b,c,d=map(int,input().split())
if a+b>d and c>d:
    print("T.T")
else:
    if c>d:
        print("Shuttle")
    elif a+b>d:
        print("Walk")
    else:
        print("~.~")