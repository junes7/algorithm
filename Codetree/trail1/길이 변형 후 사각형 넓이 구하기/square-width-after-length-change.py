arr=input().split()
w,h=int(arr[0]),int(arr[1])
w+=8
h*=3
print(w,h,w*h,sep='\n')