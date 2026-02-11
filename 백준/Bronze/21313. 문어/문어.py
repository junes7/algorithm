N = int(input())
answer = [1]
for i in range(1, N):
    if i == N-1:
        next =  min([n for n in range(1,9) if answer[i-1] != n and answer[0] != n])
    else:
        next = min([n for n in range(1,9) if answer[i-1] != n])
    answer.append(next)
print(*answer)