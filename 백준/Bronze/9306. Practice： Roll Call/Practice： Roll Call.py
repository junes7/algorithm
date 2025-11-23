import sys
input=lambda:sys.stdin.readline().rstrip()
n,names=int(input()),[]
for i in range(n):
    names+=[input()]
    names+=[input()]
for i in range(n):
    print(f'Case {i+1}: {names[2*i+1]}, {names[2*i]}')