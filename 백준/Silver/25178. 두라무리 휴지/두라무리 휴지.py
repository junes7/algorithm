import sys
input=lambda:sys.stdin.readline().rstrip()
from collections import Counter
def count_words(word):
    return Counter(word)
def remove_nouns_from_word(word):
    nouns = ['a', 'e', 'i', 'o', 'u']
    return "".join([w for w in list(word) if w not in nouns])
def duramuri_huji(word1, word2):
    answer = "NO"
    cnt1, cnt2 = count_words(word=word1), count_words(word=word2)
    word1_non_noun = remove_nouns_from_word(word=word1)
    word2_non_noun = remove_nouns_from_word(word=word2)
    condition1 = cnt1 == cnt2
    condition2 = (word1[0] == word2[0]) and (word1[-1] == word2[-1])
    condition3 = word1_non_noun == word2_non_noun
    if condition1 and condition2 and condition3:
        answer = "YES" 
    return answer
if __name__ == "__main__":
    N = int(input())
    word1 = input()
    word2 = input()
    print(duramuri_huji(word1=word1, word2=word2))