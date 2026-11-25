n=int(input())
arr=[*map(int,input().split())]
sqrt_arr=[c**2 for c in arr]
print(*sqrt_arr)