def solution(users, emoticons):
    rlt = [0, 0]
    data = [10, 20, 30, 40]
    discnt = []
    # 이모티콘 할인율 구하기
    def dfs(temp, depth):
        if depth == len(temp):
            discnt.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d
    dfs([0] * len(emoticons), 0)
    for d in range(len(discnt)):
        plus_user = 0
        profit = 0
        for user in users:
            emoticon_buy = 0
            for i in range(len(emoticons)):
                if discnt[d][i] >= user[0]:
                    emoticon_buy += emoticons[i] * ((100 - discnt[d][i]) / 100)
            if user[1] <= emoticon_buy:
                plus_user += 1
            else:
                profit += emoticon_buy
        if rlt[0] < plus_user:
            rlt = [plus_user, int(profit)]
        elif rlt[0] == plus_user:
            if rlt[1] < profit:
                rlt = [plus_user, int(profit)]
    return rlt