arr=[*map(int,input().split())]
mval=arr[0]
for c in arr[1:]:
    if mval<c:
        mval=c
print(mval)