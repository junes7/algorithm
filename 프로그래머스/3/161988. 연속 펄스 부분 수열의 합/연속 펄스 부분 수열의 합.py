def solution(sequence):
    # 두 가지 펄스 수열 (1, -1, 1, -1...) 과 (-1, 1, -1, 1...) 적용
    p1 = [x * (1 if i % 2 == 0 else -1) for i, x in enumerate(sequence)]
    p2 = [x * (-1 if i % 2 == 0 else 1) for i, x in enumerate(sequence)]
    def get_max_sum(arr):
        # 누적합 배열 구하기
        prefix_sum = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_sum[i + 1] = prefix_sum[i] + arr[i]
        # (누적합의 최댓값 - 최솟값)이 연속 부분 수열의 최대 합
        return max(prefix_sum) - min(prefix_sum)
    return max(get_max_sum(p1), get_max_sum(p2))