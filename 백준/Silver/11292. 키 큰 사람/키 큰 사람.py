while True:
    n = int(input())
    if n == 0:
        break
    max_height = 0
    name_list = []
    for _ in range(n):
        name, height = input().split()
        height = float(height)
        if height > max_height:
            name_list = [name]
            max_height = height
        elif height == max_height:
            name_list.append(name)
    print(*name_list)