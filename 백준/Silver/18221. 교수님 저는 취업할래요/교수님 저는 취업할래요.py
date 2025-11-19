n=int(input())
List=[]
tmp=[]
for i in range(n):
	#01
    a=list(map(int,input().split()))
    for j in range(len(a)):
        if a[j]==5 or a[j]==2:
            tmp.append([i,j])       
    List.append(a)
#02
x=((tmp[0][0]-tmp[1][0])**2+(tmp[0][1]-tmp[1][1])**2)**0.5
if x>=5:
    tmp.sort()
    #03
    x,y=min(tmp[0][1],tmp[1][1]),max(tmp[0][1],tmp[1][1])
    cnt=0
    for i in range(tmp[0][0],tmp[1][0]+1):
        for j in range(x,y+1): 
            if List[i][j]==1:
                cnt+=1
    #04
    if cnt>=3:
        print(1)
    else:
        print(0)
else:
    print(0)