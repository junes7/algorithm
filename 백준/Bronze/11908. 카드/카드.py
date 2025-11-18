import sys
input=lambda:sys.stdin.readline().rstrip()
n = int(input())
li = sorted(list(map(int, input().split())))
print(sum(li[:-1]))