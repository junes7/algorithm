from itertools import permutations
def is_palindrome(a):
    return a == a[::-1]
for i in range(int(input())):
    tango = []
    for j in range(int(input())):
        tango.append(input())
    printed = False
    for j in permutations(tango, 2):
        if is_palindrome("".join(j)):
            printed = True
            print("".join(j))
            break
    if not printed:
        print(0)