def count_hansu(x):
    count = 0
    for i in range(1, x+1):
        if 1 <= i < 100 :
            count += 1
        if 100 <= i < 1001 and i % 100 // 10 - i // 100 == i % 100 % 10 - i % 100 // 10:
            count += 1
    return count
N = int(input())
print(count_hansu(N))