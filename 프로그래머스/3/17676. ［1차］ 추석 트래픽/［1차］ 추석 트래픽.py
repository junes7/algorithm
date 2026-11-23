def solution(lines):
    rlt = 0
    st = []
    end = []
    for t in lines:
        time = t.split(" ")
        st.append(get_st(time[1], time[2]))
        end.append(get_time(time[1]))
    for i in range(len(lines)):
        cnt = 0
        cur_end = end[i]
        # i번째는 현재 자신의 시작시간이고, i 이하는 그 이전의 시작시간이므로 카운트 할 필요가 없다.
        for j in range(i, len(lines)):
            if cur_end > st[j] - 1000:
                cnt += 1
        rlt = max(rlt, cnt)
    return rlt
def get_time(time):
    h = int(time[:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:8])
    ms = int(time[9:])
    return (h + m + s) * 1000 + ms
def get_st(time, duration_time):
    n_time = duration_time[:-1]
    int_duration_time = int(float(n_time) * 1000)
    return get_time(time) - int_duration_time + 1