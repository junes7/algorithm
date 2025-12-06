import sys
input=lambda:sys.stdin.readline().rstrip()
n,w=int(input()),int(input())
rlt=n*10
if n==5:
    rlt+=70
elif n>=3:
    rlt+=20
if w>1000:
    rlt = 0 if rlt-15<0 else rlt-15
print(rlt)