mt,ft=map(int,input().split())
if mt>=90:
    if ft>=95:
        print(10**5)
    elif ft>=90:
        print(5*10**4)
    else:
        print(0)
else:
    print(0)