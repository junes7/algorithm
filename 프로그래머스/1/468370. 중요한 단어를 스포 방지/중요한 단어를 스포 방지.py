def solution(message, spoiler_ranges):
    words = []
    n = len(message)
    # 1. 단어와 위치 찾기
    i = 0
    while i < n:
        if message[i] == ' ':
            i += 1
            continue
        start = i
        while i < n and message[i] != ' ':
            i += 1
        end = i - 1
        word = message[start:i]
        words.append([word, start, end])

    # 2. 스포일러 위치 표시
    covered = [False] * n
    for s, e in spoiler_ranges:
        for i in range(s, e + 1):
            covered[i] = True

    # 3. 평문 단어 찾기
    normal_words = set()
    for word, start, end in words:
        spoiler_word = False
        for i in range(start, end + 1):
            if covered[i]:
                spoiler_word = True
                break
        if not spoiler_word:
            normal_words.add(word)

    # 4. 공개 진행
    opened = [False] * n
    used = set()
    rlt = 0
    for s, e in spoiler_ranges:
        for i in range(s, e + 1):
            opened[i] = True
        for word, start, end in words:
            spoiler_word = False
            for i in range(start, end + 1):
                if covered[i]:
                    spoiler_word = True
                    break
            if not spoiler_word:
                continue
            full_open = True
            for i in range(start, end + 1):
                if covered[i] and not opened[i]:
                    full_open = False
                    break
            if not full_open:
                continue
            if word not in normal_words and word not in used:
                rlt += 1
                used.add(word)
    return rlt