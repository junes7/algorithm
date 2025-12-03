import sys
input=lambda:sys.stdin.readline().rstrip()
x,d=map(int,input().split())
print("double it" if d/x>=2 else "take it")