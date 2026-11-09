a=int(input())
arr=input().split()
b,c,d,e=int(arr[0]),int(arr[1]),int(arr[2]),int(arr[3])
print(1 if a>b else 0,1 if a>c else 0,
1 if a>d else 0,1 if a>e else 0,sep='\n')