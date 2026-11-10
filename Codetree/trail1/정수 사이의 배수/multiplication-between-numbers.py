a,b=map(int,input().split())
arr=[i for i in range(a,b+1) if i%5==0 or i%7==0]
print(sum(arr),f"{sum(arr)/len(arr):.1f}")