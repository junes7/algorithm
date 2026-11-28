n=int(input())
for i in range(n):
    if i%2==1:
        for j in range(i+1):
            print('* ',end='')
        print()
    else:
        print('*')