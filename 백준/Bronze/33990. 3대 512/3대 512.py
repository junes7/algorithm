import sys
input=lambda:sys.stdin.readline().rstrip()
n,lst=int(input()),[]
for i in range(n):
    arr=[*map(int,input().split())]
    rlt=sum(arr)
    if rlt-512>=0:
        lst+=[rlt]
print(min(lst) if len(lst)>0 else -1)