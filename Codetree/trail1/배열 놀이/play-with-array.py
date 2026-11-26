n,q=map(int,input().split())
arr=[0]+[*map(int,input().split())]
for _ in range(q):
    qst=[*map(int,input().split())]
    if qst[0]==1:
        print(arr[qst[1]])
    elif qst[0]==2:
        print(0 if qst[1] not in arr else arr.index(qst[1]))
    elif qst[0]==3:
        print(*arr[qst[1]:qst[2]+1])