from itertools import combinations
def solution(n, q, ans):
    rlt = 0
    lst = [i for i in range(1, n+1)]
    index = list(filter(lambda i: ans[i] == 0, range(len(ans))))    # 하나도 못 맞춘 케이스 찾기(ans[i]=0)
    m = len(ans)
    for i in index:     # 조합에 사용할 필요 없는 숫자 제거
        for j in q[i]:
            try: lst.remove(j)
            except: pass
    for c in combinations(lst, 5):  # 가능한 모든 조합 만들기
        for i in range(m):
            cnt = 0
            for j in q[i]:      # 만들어진 조합이 조건에 충족하는지 확인
                if j in c:
                    cnt += 1
            if cnt != ans[i]:
                break  
        else:   # break 안 걸리면 조건에 모두 충족한 조합
            rlt += 1            
    return rlt