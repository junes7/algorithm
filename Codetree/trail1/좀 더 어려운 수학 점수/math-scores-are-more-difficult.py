arr=input().split()
am,ae=int(arr[0]),int(arr[1])
arr1=input().split()
bm,be=int(arr1[0]),int(arr1[1])
if am>bm or (am==bm and ae>be):
    print('A')
else:
    print('B')