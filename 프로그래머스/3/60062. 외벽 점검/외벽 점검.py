from itertools import permutations
def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w+n for w in weak]  # 선형으로
    for i, st in enumerate(weak):
        for friends in permutations(dist):  # 순열 이용
            cnt = 1
            p = st
            # 친구 조합 배치
            for friend in friends:
                p += friend
                # 끝 포인트까지 도달 못했을 때
                if p < weak_point[i+L-1]:
                    cnt += 1  # 친구 더 투입
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    p = [w for w in weak_point[i+1:i+L]
                                if w > p][0]
                else:  # 끝 포인트까지 도달
                    cand.append(cnt)
                    break
    return min(cand) if cand else -1