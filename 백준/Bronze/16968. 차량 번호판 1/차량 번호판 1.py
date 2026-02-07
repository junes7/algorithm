import sys
input=lambda:sys.stdin.readline().rstrip()
forms = {'c': 26, 'd': 10}
s = input()
rlt = forms[s[0]]
for i in range(1, len(s)):
    mul = forms[s[i]]
    if s[i] == s[i - 1]:
        mul -= 1
    rlt *= mul
print(rlt)