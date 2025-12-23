import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
for i in range(5):
    for _ in range(n):
        if i<4 and i%2==0:
            print('@'*(n*5))
        else:
            print('@'*n)