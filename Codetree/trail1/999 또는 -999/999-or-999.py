arr=[*map(int,input().split())]
max_val,min_val=arr[0],arr[0]
for c in arr[1:]:
    if c==999 or c==-999:
        break
    if max_val<c:
        max_val=c
    if min_val>c:
        min_val=c
print(max_val,min_val)