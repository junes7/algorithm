import sys
input=lambda:sys.stdin.readline().rstrip("\n")
a = int(input())
def binary_search(target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if target == mid ** 2: 
            result = mid
            break
        elif target > mid ** 2: start = mid + 1
        else: end = mid - 1
    return result
print(binary_search(a, 0, a))