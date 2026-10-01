from collections import Counter
from itertools import combinations
def solution(orders, course):
    rlt = []
    for c in course:
        menus = []
        for order in orders:
            menus += combinations(sorted(order), c)
        counter = Counter(menus)
        # 최소 2명 이상의 손님으로 부터 주문된 조합일 때
        if len(counter) > 0 and max(counter.values()) > 1: 
            # 가장 많이 주문한 코스 메뉴를 추가
            for menu in counter:
                if counter[menu] == max(counter.values()):
                    rlt.append("".join(menu))
    return sorted(rlt)