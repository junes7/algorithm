arr=list(map(int,input().split()))
t,l=sum(arr),len(arr)
print(f"{t}\n{t//l}\n{t-(t//l)}")