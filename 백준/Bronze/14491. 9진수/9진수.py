import sys
input=lambda:sys.stdin.readline().rstrip()
def solve(r,n):
    if n==0:
        return r
    return solve((str(n%9) if n%9 else "0")+r,n//9)
print(solve("",int(input())))