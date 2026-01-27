inputVal = input()
values = []
question = "문제"
while (inputVal != "고무오리 디버깅 끝"):
    inputVal = input()
    if inputVal == "문제":
        values.append(question)
    if inputVal == "고무오리":
        if len(values) == 0:
            values.append(question)
            values.append(question)
        else:
            values.pop()
print("고무오리야 사랑해") if len(values) == 0 else print("힝구")