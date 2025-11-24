import sys
input=lambda:sys.stdin.readline().rstrip()
N, S = sys.stdin.readline().rstrip().split()
write_mode = True
rlt_list = []
rlt = ''
for _ in range(int(N)):
    nickname, chat = sys.stdin.readline().rstrip().split()
    if write_mode and nickname != S:
        rlt_list.append(chat)
    elif nickname == S:
        rlt = chat
        write_mode = False
print(rlt_list.count(rlt))