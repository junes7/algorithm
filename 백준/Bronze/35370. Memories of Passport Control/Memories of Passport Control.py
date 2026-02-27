import sys
input=lambda:sys.stdin.readline().rstrip()
k,s=map(int,input().split())
print(s//k+s%k)