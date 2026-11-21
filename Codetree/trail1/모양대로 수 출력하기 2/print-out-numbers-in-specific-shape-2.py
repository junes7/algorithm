n,cnt=int(input()),2
for _ in range(n):
    for _ in range(n):
        print(cnt,end=' ')
        if cnt==8:
            cnt=2
        else:
            cnt+=2
    print()