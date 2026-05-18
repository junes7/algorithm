def solution(skill, skill_trees):
    cnt = 0
    for skill_tree in skill_trees:
        s = ""                      # 하나의 스킬트리를 뽑을 때마다 s 초기화
        for ch in skill_tree:       
            if ch in skill:         # 스킬트리 중에 skill이 있다면 s에 추가
                s += ch
        if skill[:len(s)] == s:     # 만든 s를 기준으로 skill과 같다면 cnt += 1
            cnt += 1
    return cnt