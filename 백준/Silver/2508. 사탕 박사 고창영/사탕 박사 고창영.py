import sys
input=lambda:sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    input()
    A = []
    count = 0
    r, c = map(int, input().split())
    for _ in range(r):
        A.append(input())
    for i in range(r):
        for j in range(c-2):
            if A[i][j] == '>' and A[i][j+1] == 'o' and A[i][j+2] == '<':
                count += 1
    for i in range(r-2):
        for j in range(c):
            if A[i][j] == 'v' and A[i+1][j] == 'o' and A[i+2][j] == '^':
                count += 1
    print(count)