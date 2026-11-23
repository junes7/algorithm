n=int(input())
arr=[*map(float,input().split())]
avg=sum(arr)/len(arr)
print(f"{avg:.1f}","Perfect" if avg>=4.0 else "Good" if avg>=3.0 else "Poor",sep="\n")