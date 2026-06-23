def solution(n, wires):
    rlt = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        # 집합연산자 & : 교집합 연산,   집합연산자 update : 여러데이터를 한번에 추가
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        rlt = min(rlt, abs(2 * len(s) - n))
    return rlt