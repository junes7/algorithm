import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
p_list=['G...','.I.T','..S.']
for i in range(len(p_list)):
    str=""
    for ch in p_list[i]:
        str+=ch*n;
    for j in range(n):
        print(str)