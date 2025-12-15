import sys
input=lambda:sys.stdin.readline().rstrip()
for i in range(int(input())):
    a,b=map(int,input().split())
    print((a//b)**2)