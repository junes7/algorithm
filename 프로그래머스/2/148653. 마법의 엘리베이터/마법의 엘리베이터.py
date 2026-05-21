def solution(storey):
    rlt = 0
    while storey:
        remainder = storey % 10
        # 6 ~ 9
        if remainder > 5:
            rlt += (10 - remainder)
            storey += 10
        # 0 ~ 4
        elif remainder < 5:
            rlt += remainder
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            rlt += remainder
        storey //= 10
    return rlt