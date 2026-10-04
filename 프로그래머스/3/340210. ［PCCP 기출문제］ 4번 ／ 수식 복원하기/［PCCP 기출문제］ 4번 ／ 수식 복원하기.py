def NToTen(n, num):
    if len(num)==1: return int(num)
    numb = 0
    for idx in range(len(num)):
        numb += int(num[idx])*(n**(len(num)-1-idx))
    return numb
def TenToN(n, num):
    if num==0: return "0"
    rlt = ""
    for idx in range(2,-1,-1):
        div = num // (n**idx)
        if rlt or div: rlt += str(div)
        num = num % (n**idx)
    return rlt
def solution(expressions):
    rlt, rlt_format = [], []
    max_format, hint = 0, []
    for e in expressions:
        num1, func, num2, _, ans = e.split(" ")
        for idx in range(len(num1)): max_format = max(max_format, int(num1[idx]))
        for idx in range(len(num2)): max_format = max(max_format, int(num2[idx]))
        if ans != "X": 
            hint.append(e)
            for idx in range(len(ans)): max_format = max(max_format, int(ans[idx]))
        else: rlt.append(e)
    for n in range(max_format+1, 10):
        check = 1
        for h in hint:
            num1, func, num2, _, ans = h.split(" ")
            num1, num2, ans = NToTen(n, num1), NToTen(n, num2), NToTen(n, ans)
            if (func == '+') and (num1+num2!=ans): 
                check = 0
                break
            if (func == '-') and (num1-num2!=ans): 
                check = 0
                break
        if check: 
            rlt_format.append(n)
    for idx in range(len(rlt)):
        num1, func, num2, _, ans = rlt[idx].split(" ")
        ans_set = set()
        for a in rlt_format:
            num_1, num_2 = NToTen(a, num1), NToTen(a, num2)
            if func=="+": ans_set.add(str(TenToN(a, num_1+num_2)))
            if func=="-": ans_set.add(str(TenToN(a, num_1-num_2)))
        if len(ans_set)==1:
            rlt[idx] = ' '.join([num1, func, num2, _, list(ans_set)[0]])
        else: rlt[idx] = ' '.join([num1, func, num2, _, "?"])     
    return rlt