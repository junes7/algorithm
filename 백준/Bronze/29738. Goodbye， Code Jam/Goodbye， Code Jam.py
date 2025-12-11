import sys
input=lambda:sys.stdin.readline().rstrip()
for i in range(int(input())):
    n=int(input())
    rlt="Round 1"
    if n<=25:
        rlt="World Finals"
    elif n<=1000:
        rlt="Round 3"
    elif n<=4500:
        rlt="Round 2"
    print("Case #%d: %s" % (i+1,rlt))