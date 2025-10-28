import sys
input=lambda:sys.stdin.readline().rstrip()
hurtFinger = int(input())
maxRepeat = int(input())
rlt,hurtCount = 0,0
# if hurtfinger is 1 or 5
if hurtFinger == 1:
    if maxRepeat == 0:
        rlt += hurtFinger-1
    else:
        rlt += 8*maxRepeat
elif hurtFinger == 5:
    if maxRepeat == 0:
        rlt += hurtFinger-1
    else:
        rlt += 4 + 8*(maxRepeat)
# else hurtfinger is 2,3,4
else:
    if maxRepeat == 0:
        rlt += hurtFinger-1
    else:
        rlt += 4*(maxRepeat) + 1
        if maxRepeat % 2 == 0:
            rlt += hurtFinger-2
        else:
            rlt += 4-hurtFinger
print(rlt)