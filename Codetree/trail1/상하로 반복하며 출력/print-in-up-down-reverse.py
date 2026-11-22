n=int(input())
for i in range(n):
    for j in range(n):
        print(i+1 if j%2==0 else n-i,end='')
    print()