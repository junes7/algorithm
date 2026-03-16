from itertools import permutations
# input
n = int(input())
k = int(input())
card = []
int_list = []
# make the card list(str)
for _ in range(n):
    card.append(input())
# make the combination list(int)
for i in permutations(card, k):
    int_list.append(int(''.join(i)))
print(len(set(int_list)))