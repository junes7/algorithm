import sys,math
input=lambda:sys.stdin.readline().rstrip()
C = int(input())
for _ in range(C):
    complexity, *params = input().split()
    max_input_size, test_count, time_limit = map(int, params)
    if complexity == 'O(N)':
        operations = max_input_size
    elif complexity == 'O(N^2)':
        operations = max_input_size ** 2
    elif complexity == 'O(N^3)':
        operations = max_input_size ** 3
    elif complexity == 'O(2^N)':
        operations = 2 ** max_input_size
    else:  # complexity == 'O(N!)'
        if max_input_size > 12:  # 12보다 크면 무조건 TLE
            print("TLE!")
            continue
        operations = math.factorial(max_input_size)
    if operations * test_count <= 10**8 * time_limit:
        print("May Pass.")
    else:
        print("TLE!")