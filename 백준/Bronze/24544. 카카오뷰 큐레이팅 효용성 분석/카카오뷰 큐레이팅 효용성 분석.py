import sys
input=lambda:sys.stdin.readline().rstrip()
def kakao_view_curating_check(interest_list, register_list):
    total_interest, not_register_interest = 0, 0
    for interest, register in zip(interest_list, register_list):
        total_interest += interest
        if not register:
            not_register_interest += interest 
    return total_interest, not_register_interest
if __name__ == "__main__":
    N = int(input())
    interest_list = list(map(int, input().split()))
    register_list = list(map(int, input().split()))
    total_interest, not_register_interest = kakao_view_curating_check(
        interest_list=interest_list, register_list=register_list
    )
    print(total_interest)
    print(not_register_interest)