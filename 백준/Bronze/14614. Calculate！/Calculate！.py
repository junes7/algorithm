import sys
input=lambda:sys.stdin.readline().rstrip()
a,b,c=map(int,input().split())
for _ in range(c%2):
    a^=b;
print(a)