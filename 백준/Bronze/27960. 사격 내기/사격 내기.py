import sys
input=lambda:sys.stdin.readline().rstrip()
a,b=map(int,input().split())
bin_a,bin_b=bin(a),bin(b)
rlt=int(bin(a^b)[2:],2)
print(rlt)