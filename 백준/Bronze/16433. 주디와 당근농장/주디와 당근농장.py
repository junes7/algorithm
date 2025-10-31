import sys
input=lambda:sys.stdin.readline().rstrip()
def case_1(a):
    for i in range(1, a+1):
        if i % 2 == 0:
            for j in range(1, a+1):
                if j % 2 == 0:
                    print(".", end="")
                else:
                    print("v", end="")
            print("\n", end="")
        else:
            for j in range(1, a+1):
                if j % 2 == 0:
                    print("v", end="")
                else:
                    print(".", end="")
            print("\n", end="")
def case_2(a):
    for i in range(1, a+1):
        if i % 2 == 0:
            for j in range(1, a+1):
                if j % 2 == 0:
                    print("v", end="")
                else:
                    print(".", end="")
            print("\n", end="")
        else:
            for j in range(1, a+1):
                if j % 2 == 0:
                    print(".", end="")
                else:
                    print("v", end="")
            print("\n", end="")
a = sys.stdin.readline().rstrip()
lst = list(map(int, a.split()))
if (lst[1] + lst[2]) % 2 != 0:
    case_1(lst[0])
else:
    case_2(lst[0])