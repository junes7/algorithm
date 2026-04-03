N = int(input())
dancePeople = {"ChongChong"}
for _ in range(N):
    A, B = input().split()
    if A in dancePeople:
        dancePeople.add(B)
    if B in dancePeople:
        dancePeople.add(A)
print(len(dancePeople))