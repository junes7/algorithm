import sys
input=lambda:sys.stdin.readline().rstrip("\n")
s,t,rlt=input(),input(),""
for c in t:
    if c not in s:
        rlt+=c
print(rlt)