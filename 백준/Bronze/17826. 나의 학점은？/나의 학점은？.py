import sys
input=lambda:sys.stdin.readline().rstrip()
arr=[*map(int,input().split())]
idx=arr.index(int(input()))+1
if idx<=5:
    print("A+")
elif idx<=15:
    print("A0")
elif idx<=30:
    print("B+")
elif idx<=35:
    print("B0")
elif idx<=45:
    print("C+")
elif idx<=48:
    print("C0")
else:
    print("F")