import sys
input=lambda:sys.stdin.readline().rstrip()
def matched_string(h):
    if h<2: return int(not h)
    return int(('4'*(h%2)) + ('8'*(h//2)))
print(matched_string(int(input())))