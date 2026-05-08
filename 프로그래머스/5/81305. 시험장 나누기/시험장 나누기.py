import sys
sys.setrecursionlimit(int(1e6))

def find_root(links) :
    length = len(links)
    visited = [False]*length
    for i in range(length) :
        if not visited[i] :
            result = i
            q = [i]
            visited[i] = 0
            while q :
                node = q.pop()
                for leaf in links[node] :
                    if leaf > -1 and not visited[leaf] :
                        visited[leaf] = True
                        q.append(leaf)
    
    return result
    
def search(node, target, num, links) :
    if node == -1 :
        return 0, 0
    
    left, right = links[node]
    left_cnt, left_val = search(left, target, num, links)
    right_cnt, right_val = search(right, target, num, links)
    tot_cnt = left_cnt + right_cnt
    
    result_sum = left_val + right_val + num[node] 
    
    if result_sum <= target :
        return tot_cnt, result_sum

    if min(left_val,right_val) + num[node] <= target :
        return tot_cnt + 1, min(left_val,right_val) + num[node]

    return tot_cnt + 2, num[node]

def binary_search(root, start, end, k, num, links) :
    result = end
    while start <= end :
        mid = (start + end) // 2
        div_cnt, _ = search(root, mid, num, links)
        if div_cnt > k-1 :
            start = mid+1
        else :
            result = min(result, mid)
            end = mid-1
    
    return result
    
def solution(k, num, links):
    length = len(links)
    root = find_root(links)
    start, end = max(num), sum(num)
    rlt = binary_search(root, start, end, k, num, links)

    return rlt