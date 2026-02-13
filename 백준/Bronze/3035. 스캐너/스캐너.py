import sys
input = lambda:sys.stdin.readline().rstrip("\n")
r, c, zr, zc = map(int, input().split())
arr = [input() for _ in range(r)]
for i in range(r):
	ans = ''
	for j in range(c):
		ans += arr[i][j] * zc
	for j in range(zr):
		print(ans)