import sys
input=lambda:sys.stdin.readline().rstrip()
n,iskor=int(input()),False
arr=[input() for i in range(n)]
for c in arr:
    if c=="korea":
        iskor=True
    if c=="yonsei":
        print("Yonsei Won!" if iskor==False else "Yonsei Lost...")
        break