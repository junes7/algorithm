# 110 다 추출하고 111앞에 넣기
def solution(s):
    rlt = []
    for string in s:
        stack = []
        count_110 = 0
        for str in string:
            # 110이 나온 경우
            if(len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and str == '0'):
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str)
        # 110을 모두 제거했으므로 남은 문자열에서 연속된 1이 존재하는 곳은 한 곳밖에 없다.
        count_1 = 0
        for s in stack[::-1]:
            if s == '0':
                break
            else:
                count_1 += 1
        rlt.append(''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1)
    return rlt