n,d,cnt=int(input()),1,0
while n>1:
    n//=d
    d+=1
    cnt+=1
print(cnt)