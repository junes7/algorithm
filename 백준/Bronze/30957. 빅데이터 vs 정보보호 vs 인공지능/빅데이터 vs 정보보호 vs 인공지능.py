import sys,math
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
st,tmp,rlt=input(),"BSA",""
num=[st.count('B'),st.count('S'),st.count('A')]
maxn=max(num)
for i in range(len(num)):
    if num[i]==maxn:
        rlt+=tmp[i]
print("SCU" if num[0]==num[1] and num[1]==num[2] and num[0]==num[2] else rlt)