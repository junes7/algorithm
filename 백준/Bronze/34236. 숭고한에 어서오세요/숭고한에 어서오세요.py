import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
arr=[*map(int,input().split())]
print(arr[-1]+(arr[1]-arr[0]))