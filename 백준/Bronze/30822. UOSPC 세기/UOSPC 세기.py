import sys
input=lambda:sys.stdin.readline().rstrip()
n,st=int(input()),input()
c=[st.count(i) for i in "uospc"]
print(min(c))