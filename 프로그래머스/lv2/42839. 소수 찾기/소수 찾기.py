from itertools import permutations
import math
def check(n):
    k = math.sqrt(n)
    if n < 2:
        return False
    else:
        for i in range(2, int(k)+1):
            if n % i == 0:
                return False
        return True
def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        perlist = list(permutations(numbers, i))
        for j in range(len(perlist)):
            num = int(''.join(map(str, perlist[j])))
            if check(num):
                if num not in answer:
                    answer.append(num)
    answer = len(set(answer))
    return answer