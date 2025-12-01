import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
print("Time limit exceeded" if n**2/10**8>1 else "Accepted")