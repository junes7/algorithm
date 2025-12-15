import sys
input=lambda:sys.stdin.readline().rstrip()
arr=[*map(int,input().split())]
idx=arr.index(int(input()))
if idx+1<=5:
    print("A+")
elif idx+1<=15:
    print("A0")
elif idx+1<=30:
    print("B+")
elif idx+1<=35:
    print("B0")
elif idx+1<=45:
    print("C+")
elif idx+1<=48:
    print("C0")
else:
    print("F")