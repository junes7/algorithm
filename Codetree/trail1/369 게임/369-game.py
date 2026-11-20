n=int(input())
for i in range(1,n+1):
    st=str(i)
    if i%3==0 or '3' in st or '6' in st or '9' in st:
        print(0,end=' ')
    else:
        print(i,end=' ')