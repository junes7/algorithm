import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n=int(input())
print("Even" if n%4==0 else "Odd" if n%2==0 else "Either")