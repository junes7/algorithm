import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n,x=int(input()),int(input())
tmp=n*(1-x/100)
print(f"{(n/tmp-1)*100:.6f}")