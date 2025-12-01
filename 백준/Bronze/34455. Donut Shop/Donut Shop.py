import sys
input=lambda:sys.stdin.readline().rstrip()
d=int(input())
for i in range(int(input())):
    op=input()
    q=int(input())
    d=d+q if op=="+" else d-q
print(d)