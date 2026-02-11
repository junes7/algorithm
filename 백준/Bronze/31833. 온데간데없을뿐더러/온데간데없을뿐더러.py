import sys
input=lambda:sys.stdin.readline().rstrip("\n")
N = int(input())
A = int("".join(input().split()))
B = int("".join(input().split()))
print(A if A<B else B)