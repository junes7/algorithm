import sys
input=lambda:sys.stdin.readline().rstrip()
y,c,p=map(int,input().split())
print(min(y//1,c//2,p//1))