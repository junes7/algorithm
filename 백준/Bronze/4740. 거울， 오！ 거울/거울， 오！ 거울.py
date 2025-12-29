import sys
input=lambda:sys.stdin.readline().rstrip("\n")
while True:
    st=input()
    if st=="***": break
    print(st[::-1])