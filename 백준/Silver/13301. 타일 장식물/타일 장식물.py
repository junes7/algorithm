import sys
input=lambda:sys.stdin.readline().rstrip("\n")
a,b=1,1
for _ in range(int(input())-1):
    a,b=b,a+b
print((a+b)*2)