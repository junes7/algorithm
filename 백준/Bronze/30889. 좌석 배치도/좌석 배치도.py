import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
seat=[["." for _ in range(20)] for _ in range(10)]
for _ in range(n):
    data=input()
    r,c=data[0],int(data[1:])
    seat[ord(r)-65][c-1]="o"
for s in seat:
    print("".join(s))