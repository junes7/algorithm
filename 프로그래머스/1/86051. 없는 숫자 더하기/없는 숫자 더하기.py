def solution(numbers):
    r=0
    for i in range(10):
        if i not in numbers:
            r+=i
    return r