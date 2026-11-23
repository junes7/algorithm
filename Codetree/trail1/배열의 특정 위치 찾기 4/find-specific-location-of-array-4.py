arr=[*map(int,input().split())]
cnt,tot=0,0
for i in range(10):
    if arr[i]==0:
        break
    if arr[i]%2==0:
        tot+=arr[i]
        cnt+=1
print(cnt,tot)