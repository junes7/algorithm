def solution(data, col, row_begin, row_end):
    rlt = 0
    #col번째 컬럼 기준으로 정렬, 동일하면 기본키 기준으로 내림차순 정렬함
    data.sort(key=lambda d: (d[col-1],-d[0]))
    # 여러 튜플 중 row_begin에서 시작해 row_end까지 반복
    S_i = []
    for i in range(row_begin-1, row_end) :
        tmp = 0
        for j in (data[i]) :
            tmp += j % (i+1) #i번째 행의 튜플에 대해 각 컬럼을 i로 나눈 나머지들의 합을 구함
        S_i.append(tmp)
    rlt = bitwiseXOR(S_i) # S_i를 XOR함
    return rlt
# XOR하는 함수
def bitwiseXOR(arr) :
    rlt = arr[0]
    for a in range(1,len(arr)):
        rlt ^= arr[a]
    return rlt