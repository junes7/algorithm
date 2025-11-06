import sys
input=lambda:sys.stdin.readline().rstrip()
N = int(input())
for i in range(N):
    print("@" * N + " " * 3 * N + "@" * N)
for i in range(N):
    print("@" * N + " " * 2 * N + "@" * N)
for i in range(N):
    print("@" * 3 * N)
for i in range(N):
    print("@" * N + " " * 2 * N + "@" * N)
for i in range(N):
    print("@" * N + " " * 3 * N + "@" * N)