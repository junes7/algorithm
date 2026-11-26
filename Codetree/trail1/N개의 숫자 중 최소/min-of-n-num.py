n = int(input())
a = [*map(int, input().split())]
min_val,cnt=a[0],0
for c in a[1:]:
    if min_val>c:
        min_val=c
for c in a:
    if c==min_val:
        cnt+=1
print(min_val,cnt)