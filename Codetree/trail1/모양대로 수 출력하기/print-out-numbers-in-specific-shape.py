n=int(input())
for i in range(n):
    print(end="  "*i)
    for j in range(n-i,0,-1):
        print(j,end=" ")
    print()