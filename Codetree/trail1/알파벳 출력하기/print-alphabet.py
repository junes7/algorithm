n,ch=int(input()),65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end="")
        if chr(ch)=='Z':
            ch=65
        else:
            ch+=1
    print()