import sys
input=lambda:sys.stdin.readline().rstrip()
w1,h1,w2,h2=int(input()),int(input()),int(input()),int(input())
print(4+2*max(w1,w2)+2*(h1+h2))