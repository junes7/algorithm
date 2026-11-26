import sys
arr=[*map(int,input().split())]
mval=-sys.maxsize
for c in arr:
    if mval<c:
        mval=c
print(mval)