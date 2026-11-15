n,ch=int(input()),65
for i in range(n):
    print(end="  "*i)
    for _ in range(n-i):
        print(chr(ch),end=" ")
        if chr(ch)=='Z':
            ch=65
        else:
            ch+=1
    print()