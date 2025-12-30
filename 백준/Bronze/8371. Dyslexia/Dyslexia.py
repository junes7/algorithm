import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n,a,b,rlt=int(input()),input(),input(),0
for i in range(n):
    if a[i]!=b[i]:
        rlt+=1
print(rlt)