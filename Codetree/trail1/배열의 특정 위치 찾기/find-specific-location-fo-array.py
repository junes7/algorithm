arr=list(map(int,input().split()))
tot,cnt=0,0
avg=0.0
for i in range(1,11):
    if i%2==0:
        tot+=arr[i-1]
    if i%3==0:
        avg+=arr[i-1]
        cnt+=1
print(tot,f"{avg/cnt:.1f}")