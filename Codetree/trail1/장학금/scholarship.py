arr=input().split()
mt,ft=int(arr[0]),int(arr[1])
if mt<90:
    print("0")
elif ft>=95:
    print("100000")
elif ft>=90:
    print("50000")
else:
    print("0")