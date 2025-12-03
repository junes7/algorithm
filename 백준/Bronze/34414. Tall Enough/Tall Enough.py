import sys
input=lambda:sys.stdin.readline().rstrip()
rlt=True
for i in range(int(input())):
    elem=int(input())
    if elem<48:
        rlt=False
        break
print(rlt)