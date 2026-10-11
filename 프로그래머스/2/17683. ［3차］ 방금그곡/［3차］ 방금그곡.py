def minute_operate(e, s):
    # HH:MM 형식의 시간을 분 단위 정수로 변환
    e_int = int(e.split(':')[0]) * 60 + int(e.split(':')[1])
    s_int = int(s.split(':')[0]) * 60 + int(s.split(':')[1])
    return e_int - s_int
def change_sharp(melody):
    # #이 붙은 음을 소문자 한 글자로 치환
    return melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
def solution(m, musicinfos):
    musicinfo_dct = {}
    record = []
    # 기억한 멜로디도 변환 필수!
    m = change_sharp(m)
    for i, musicinfo in enumerate(musicinfos):
        s, e, title, info = musicinfo.split(',')
        musicinfo_dct[i] = title
        tmp = minute_operate(e, s)
        info = change_sharp(info)
        # 음악 재생 길이만큼 늘리기/자르기
        if tmp > len(info):
            info = info * ((tmp // len(info)) + 1)
        info = info[:tmp]   
        # 멜로디 매칭 확인
        if m in info:
            record.append([tmp, i])
    # 정렬: 재생 시간 내림차순(-x[0]), 입력 순서 오름차순(x[1])
    record.sort(key=lambda x: (-x[0], x[1])) 
    return musicinfo_dct[record[0][1]] if record else "(None)"