import sys
input=lambda:sys.stdin.readline().rstrip()
d,w,n=float(input()),float(input()),int(input())
print("YES" if n<=d/w*3.14159 else "NO")