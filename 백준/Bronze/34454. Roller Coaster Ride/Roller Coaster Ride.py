import sys
input=lambda:sys.stdin.readline().rstrip()
n,c,p=int(input()),int(input()),int(input())
print("no" if n>c*p else "yes")