n,i,cnt=int(input()),1,0
arr=[]
while cnt<2:
    arr+=[n*i]
    if (n*i)%5==0:
        cnt+=1
    i+=1
print(*arr)