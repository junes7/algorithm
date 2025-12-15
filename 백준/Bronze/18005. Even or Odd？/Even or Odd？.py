import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
print(0 if n%2==1 else 2 if n//2%2==0 else 1)