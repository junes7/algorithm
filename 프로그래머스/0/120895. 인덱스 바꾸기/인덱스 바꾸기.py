def solution(my_string, num1, num2):
    # method1 swap
    l=list(my_string)
    t=l[num1]
    l[num1]=l[num2]
    l[num2]=t
    return ''.join(l)