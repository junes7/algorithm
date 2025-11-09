import sys
input=lambda:sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    L, R, S = map(int, input().split())
    L_Check, R_Check = S - L, R - S
    if L_Check < R_Check:
        print(L_Check * 2 + 1)
    else:
        print(R_Check * 2)