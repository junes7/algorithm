import sys
input=lambda:sys.stdin.readline().rstrip("\n")
def solve(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            return False
    return True
arr=[*map(int,input().split())]
print('Good' if solve(arr) else 'Bad')