from collections import defaultdict
def solution(genres, plays):
    answer = []
    music = defaultdict(list)
    musicSum = defaultdict(int)
    for i, [g, p] in enumerate(zip(genres, plays)):
        music[g].append((-p, i))
        musicSum[g] += p
    musicSum = [[musicSum[k], k] for k in musicSum]
    musicSum.sort(reverse=True)
    for val, key in musicSum:
        musicList = sorted(music[key])
        for p, i in musicList[:2]:
            answer.append(i)
    return answer