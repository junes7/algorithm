import sys
input=lambda:sys.stdin.readline().rstrip()
c,b=map(int,input().split())
print(int(c/b) if c%b==0 else f"{c/b:.6f}")