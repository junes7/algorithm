n=int(input())
arr=[*map(int,input().split())]
even_arr=[arr[i] for i in range(n) if arr[i]%2==0]
print(*even_arr[::-1])