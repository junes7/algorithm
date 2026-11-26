arr=[input().split() for i in range(5)]
for i in range(5):
    for j in range(3):
        arr[i][j]=chr(ord(arr[i][j])-32)
        print(arr[i][j],end=' ')
    print()