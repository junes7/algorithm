N = list(map(int, input()))
if (N.count(2) + N.count(0) + N.count(1) + N.count(8)) == len(N):
    if (2 in N) and (0 in N) and (1 in N) and (8 in N):
        if N.count(2) == N.count(0) == N.count(1) == N.count(8):
            print(8)
        else:
            print(2)
    else:
        print(1)
else:
    print(0)