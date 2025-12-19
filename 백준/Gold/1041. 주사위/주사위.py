import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
arr=[*map(int,input().split())]
rlt,n_list,n_cnt=0,[],[]
if n==1:
    arr.sort()
    for i in range(5):
        rlt+=arr[i]
else:
    n_list+=[min(arr[0],arr[5])]
    n_list+=[min(arr[1],arr[4])]
    n_list+=[min(arr[2],arr[3])]
    n_list.sort()
    rlt+=n_list[0]*(4*(n-2)*(n-1)+(n-2)**2)
    rlt+=(n_list[0]+n_list[1])*(4*(n-2)+4*(n-1))
    rlt+=(sum(n_list))*4
print(rlt)