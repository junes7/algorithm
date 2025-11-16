import sys
input=lambda:sys.stdin.readline().rstrip()
def make_prefix_sum(n, array):
    prefix_sum = [0]*(n+1)
    start = array[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + abs(array[i] - start)
        start = array[i]
    return prefix_sum
def find_change(prefix_sum, array):
    result = []
    for start, end in array:
        result.append(prefix_sum[end-1] - prefix_sum[start-1])
    return result
def main():
    inputs = map(int, sys.stdin.read().split())
    n, q = next(inputs), next(inputs)
    prefix_sum = make_prefix_sum(n, [next(inputs) for _ in range(n)])
    sys.stdout.write('\n'.join(map(str, find_change(prefix_sum, [(next(inputs), next(inputs)) for _ in range(q)]))))
if __name__ == '__main__':
    main()