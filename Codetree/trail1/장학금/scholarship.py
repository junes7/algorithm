arr=input().split()
mt,ft=int(arr[0]),int(arr[1])
if mt>=90 and ft>=95:
    print(100000)
elif mt>=90 and ft>=90:
    print(50000)
else:
    print(0)