N, M  = map(int, input().split())
friend_count = dict(zip(range(1, N + 1), [0] * N))
for _ in range(M):
    A, B = map(int, input().split())
    friend_count[A] += 1
    friend_count[B] += 1
for k, v in sorted(friend_count.items(), key=lambda x: x[0]):
    print(v)