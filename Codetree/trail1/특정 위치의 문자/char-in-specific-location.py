arr=['L','E','B','R','O','S']
ch=input()
if ch in arr:
    print(arr.index(ch))
elif ch not in arr:
    print("None")