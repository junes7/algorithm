import sys
input=lambda:sys.stdin.readline().rstrip()
for i in range(int(input())):
    n=int(input())
    if n<=25:
        print("Case #%d: %s" % (i+1,"World Finals"))
    elif n<=1000:
        print("Case #%d: %s" % (i+1,"Round 3"))
    elif n<=4500:
        print("Case #%d: %s" % (i+1,"Round 2"))
    else:
        print("Case #%d: %s" % (i+1,"Round 1"))