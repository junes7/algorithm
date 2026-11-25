n=int(input())
arr=[*map(int,input().split())]
even_arr=[c for c in arr if c%2==0]
print(*even_arr)