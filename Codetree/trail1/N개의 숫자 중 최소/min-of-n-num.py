n = int(input())
a = [*map(int, input().split())]
min_val=a[0]
for c in a[1:]:
    if min_val>c:
        min_val=c
print(min_val,a.count(min_val))