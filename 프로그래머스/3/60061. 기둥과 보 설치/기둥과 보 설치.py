def check_build(answer):
    for x, y, a in answer:
        # 기둥인 경우
        if a == 0:
            # 좌표가 바닥에 해당 x
            # 좌표 아래에 기둥이 존재 x
            # 보의 한 쪽 위 x
            if (y != 0 and
                [x, y - 1, 0] not in answer and
                [x - 1, y, 1] not in answer and
                [x, y, 1] not in answer):
                return False
        # 보인 경우
        else:
            # 아래애 기둥 존재 x
            # 양쪽에 보 존재 x
            if ([x, y - 1, 0] not in answer and
                [x + 1, y - 1, 0] not in answer and
                ([x - 1, y, 1] not in answer or
                 [x + 1, y, 1] not in answer)):
                return False
    return True
def solution(n, build_frame):
    rlt = []
    for x, y, a, b in build_frame:
        # 삭제라면
        if b == 0:
            rlt.remove([x, y, a])
            # 삭제 후, check가 통과되지 못한다면, 재설치
            if not check_build(rlt):
                rlt.append([x, y, a])
        # 설치라면
        elif b == 1:
            rlt.append([x, y , a])
            # 설치 후, check가 통과되지 못한다면, 삭제처리
            if not check_build(rlt):
                rlt.remove([x, y, a])

    rlt.sort(key= lambda x : (x[0], x[1], x[2]))
    return rlt