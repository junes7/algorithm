arr=[*map(int,input().split())]
tot,cnt=0,0
for i in range(10):
    if arr[i]==0:
        break
    tot+=arr[i]
    cnt+=1
print(tot,f"{tot/cnt:.1f}")