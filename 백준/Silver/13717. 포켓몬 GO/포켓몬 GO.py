import sys
input=lambda:sys.stdin.readline().rstrip()
def poketmon_go(poketmon_list):
    total_evol_num = 0
    eval_info = []
    for poket_idx, poketmon_info in enumerate(poketmon_list):
        poketmon, k, m = poketmon_info[0], poketmon_info[1], poketmon_info[2]
        poketmon_evol_num = 0
        while m >= k:
            m -= k
            m += 2
            poketmon_evol_num += 1
        total_evol_num += poketmon_evol_num
        eval_info.append([poketmon, poketmon_evol_num, poket_idx])
    max_evol_poketmon = sorted(eval_info, key=lambda x: (x[1], -x[2]))[-1][0]
    return total_evol_num, max_evol_poketmon
if __name__ == "__main__":
    poketmon_list = []
    for _ in range(int(input())):
        poketmon = input()
        k, m = map(int, input().split())  
        poketmon_list.append((poketmon, k, m))      
    answer = poketmon_go(poketmon_list=poketmon_list)
    print(answer[0])
    print(answer[1])