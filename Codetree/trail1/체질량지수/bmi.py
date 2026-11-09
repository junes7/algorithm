arr=input().split()
h,w=int(arr[0]),int(arr[1])
b=10000*w//(h*h)
print(b)
if b>=25:
    print("Obesity")