import sys
input=lambda:sys.stdin.readline().rstrip()
a,b=input(),input()
rlt=[abs(ord(a[0])-ord(b[0])),abs(ord(a[1])-ord(b[1]))]
print(rlt[1] if rlt[0]>rlt[1] else rlt[0],
rlt[0] if rlt[0]>rlt[1] else rlt[1])