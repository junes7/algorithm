r,g,b=map(int,input().split())
r1,g1,b1=r/255,g/255,b/255
k=1-max(r1,g1,b1)
c,m,y=0,0,0
if k!=1:
    c=(1-r1-k)/(1-k)
    m=(1-g1-k)/(1-k)
    y=(1-b1-k)/(1-k)
print(c,m,y,k)