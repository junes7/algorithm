def num(sum,k):
    room=sum%k
    c=0
    if room==0: c=sum//k
    else: c=(sum//k)+1
    return c;

n,k=map(int,input().split())
boy=[0]*6
girl=[0]*6
count=0
for i in range(n):
    e,y=map(int,input().split())
    if e==0: girl[y-1]+=1
    else: boy[y-1]+=1
sum=0
for i in range(0,6,2):
    if i==0:
        sum=boy[i]+boy[i+1]+girl[i]+girl[i+1]
        count+=num(sum,k);
    else:
        sum = boy[i] + boy[i + 1];
        count += num(sum, k);
        sum = girl[i] + girl[i + 1];
        count += num(sum, k);
print(count)