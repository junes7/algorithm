n,elem=int(input()),0
arr=[1,n]
while True:
    elem=arr[-1]+arr[-2]
    if elem>=100:
        arr+=[elem]
        break
    arr.append(elem)
print(*arr)