import sys
input=lambda:sys.stdin.readline().rstrip()
n, k = map(int, input().split())
list1 = []
for i in range(n):
    list1.append(list(map(int, input().split())))
for i in range(n):
    for l in range(k):
        for j in range(n):
            for m in range(k):
                print(list1[i][j], end = ' ')
        print()