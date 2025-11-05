import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
num=list(map(int,input().split()))
count0=0
count1=0
count_1=0
for i in range(n):
    if num[i]==0:
        count0=count0+1
    elif num[i]==1:
        count1=count1+1
    else:
        count_1=count_1+1
if(count0>=max(count1,count_1)):
     print("INVALID")
elif(count0<max(count1,count_1)):
    if(sum(num)>0):
        print("APPROVED")
    elif(sum(num)<=0):
        print("REJECTED")