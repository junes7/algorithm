from itertools import permutations
def operation(num1, num2, op):
    return str(eval(f"{num1}{op}{num2}"))
def calculate(exp,op):
    array,tmp=[],""
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)
    for o in op:
        stack=[]
        while len(array)!=0:
            tmp=array.pop(0)
            if tmp==o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array=stack   
    return abs(int(array[0]))
def solution(expression):
    op = list(permutations(['+', '-', '*'], 3))
    rlt=[]
    for i in op:
        rlt.append(calculate(expression, i))
    return max(rlt)