import sys,math
input=lambda:sys.stdin.readline().rstrip("\n")
for _ in range(int(input())):
    n=int(input())
    t=math.sqrt(n)
    print(1 if t==int(t) else 0)