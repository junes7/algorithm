n,cnt=int(input()),0
for _ in range(n):
    arr=[*map(int,input().split())]
    if sum(arr)/4>=60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)