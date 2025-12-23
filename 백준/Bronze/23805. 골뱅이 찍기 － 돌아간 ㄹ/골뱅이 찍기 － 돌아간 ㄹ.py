import sys
input=lambda:sys.stdin.readline().rstrip()
n=int(input())
rlt=['' for _ in range(n*5)]
for i in range(n*5):
    if i<n:
        rlt[i]=f"{'@'*(n*3)}{' '*n}{'@'*n}"
    elif n<=i<n*5-n:
        for j in range(5):
            rlt[i]+=('@' if j%2==0 else ' ')*n
    else:
        rlt[i]=f"{'@'*n}{' '*n}{'@'*(n*3)}"
print("\n".join(rlt))