import sys
input=lambda:sys.stdin.readline().rstrip()
s,d,t=int(input()),float(input()),float(input())
print("MADE IT" if d/(s*5280/3600)<=t else "FAILED TEST")