def solution(files):
    rlt = []
    for file in files:
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                number += file[i]
            elif not number:
                head += file[i]
            else:
                tail = file[i:]
                break
        rlt.append((head, number, tail))
    rlt.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(s) for s in rlt]