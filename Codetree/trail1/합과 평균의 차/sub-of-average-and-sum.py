arr=list(map(int,input().split()))
t,avg=sum(arr),sum(arr)//len(arr)
print(f"{t}\n{avg}\n{t-avg}")