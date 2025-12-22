import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
for i in range(5):
    for _ in range(n):
        print('@'*(n*5 if i%2==0 else n))