import sys
input=lambda:sys.stdin.readline().rstrip("\n")
from string import ascii_uppercase, ascii_lowercase
encryption = {" ": 0}
for i in range(1, len(list(ascii_uppercase)+list(ascii_lowercase))+1):
    encryption[(list(ascii_uppercase)+list(ascii_lowercase))[i-1]] = i
n = int(input())
numbers = list(map(int, input().split()))
plaintext = []
for i in input():
    plaintext.append(encryption[i])
if sorted(numbers) == sorted(plaintext):
    print("y")
else:
    print("n")