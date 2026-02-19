from sys import stdin as s
from collections import deque
N = int(s.readline())
cards = deque(map(int, s.readline().split()))
card_num = 1
removed = 0
while cards:
    if cards[0] == card_num:
        cards.popleft()
        card_num += 1
    else:
        cards.popleft()
        removed += 1
print(removed)