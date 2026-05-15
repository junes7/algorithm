def solution(order):
    rlt = 0
    belt = []
    idx = 0
    for box in range(1, len(order) + 1):
        belt.append(box)
        while (belt) and (belt[-1] == order[idx]):
            rlt += 1
            idx += 1
            belt.pop()
    return rlt