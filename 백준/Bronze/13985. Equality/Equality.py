import sys
input=lambda:sys.stdin.readline().rstrip()
eq=list(input().split())
print("YES" if int(eq[0]) + int(eq[2]) ==int(eq[4]) else "NO")