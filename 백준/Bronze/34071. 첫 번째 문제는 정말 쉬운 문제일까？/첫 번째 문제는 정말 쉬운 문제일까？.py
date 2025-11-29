import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
arr=[int(input()) for i in range(n)]
print("ez" if min(arr)==arr[0] else "hard" if max(arr)==arr[0] else "?")