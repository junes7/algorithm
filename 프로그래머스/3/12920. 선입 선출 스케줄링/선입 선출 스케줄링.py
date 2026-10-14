def solution(n, cores):
    len_cores = len(cores)
    if n < len_cores:
        return n
    n -= len_cores
    left, right = 1, max(cores) * n
    while left < right:  # 이분 탐색
        mid = (left + right) // 2
        temp = 0
        for c in cores:
            temp += mid // c
        if temp >= n:
            right = mid
        else:
            left = mid + 1
    n -= sum(map(lambda x: (right - 1) // x, cores))
    for i in range(len_cores):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1