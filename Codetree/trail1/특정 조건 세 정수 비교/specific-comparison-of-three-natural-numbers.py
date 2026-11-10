a,b,c=map(int,input().split())
mi=min(a,b,c)
print(1 if a==mi else 0,1 if a==b and b==c else 0)