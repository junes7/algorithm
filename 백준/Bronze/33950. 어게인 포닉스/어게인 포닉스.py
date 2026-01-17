import sys
input=lambda:sys.stdin.readline().rstrip("\n")
for _ in range(int(input())):
    st=input()
    if "PO" in st:
        st=st.replace("PO","PHO")
    print(st)