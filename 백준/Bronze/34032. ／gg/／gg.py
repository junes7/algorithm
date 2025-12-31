import sys
input=lambda:sys.stdin.readline().rstrip("\n")
n=int(input())
mid=n//2+(0 if n%2==0 else 1)
st=input()
print("Yes" if st.count('O')>=mid else "No")