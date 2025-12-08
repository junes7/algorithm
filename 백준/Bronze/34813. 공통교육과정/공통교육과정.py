import sys
input=lambda:sys.stdin.readline().rstrip()
cl=input()
rlt={'F':'Foundation','C':'Claves','V':'Veritas','E':'Exploration'}
print(rlt.get(cl[0]))