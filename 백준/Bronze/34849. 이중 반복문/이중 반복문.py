import sys
input=lambda:sys.stdin.readline().rstrip()
print("Time limit exceeded" if int(input())**2/10**8>1 else "Accepted")