N = int(input())
A = input().split()
removed = 0
for i in range(N):
    if i == N - removed:
        print(removed)
        quit()
    while A[i] != str(i + 1):
        del A[i]
        removed += 1
        if i == N - removed:
            print(removed)
            quit()
print(removed)