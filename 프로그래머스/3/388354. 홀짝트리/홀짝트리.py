import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
def solution(nodes, edges):
    def check_node(table, node, visited, stats):
        visited.add(node)
        # 홀수 노드
        if node % 2 == 1 and len(table[node]) % 2 == 1:
            stats[0] += 1
        # 짝수 노드
        if node % 2 == 0 and len(table[node]) % 2 == 0:
            stats[1] += 1
        # 역홀수 노드
        if node % 2 == 1 and len(table[node]) % 2 == 0:
            stats[2] += 1
        # 역짝수 노드
        if node % 2 == 0 and len(table[node]) % 2 == 1:
            stats[3] += 1
        for n in table[node]:
            if n in visited:
                continue
            check_node(table, n, visited, stats)
        return
    tables = defaultdict(set)
    for edge in edges:
        node1, node2 = edge[0], edge[1]
        tables[node1].add(node2)
        tables[node2].add(node1)
    visited = set()
    rlt = [0, 0]
    for node in nodes:
        if node not in visited:
            visited.add(node)
            stats = [0, 0, 0, 0]
            check_node(tables, node, visited, stats)
            # 홀수노드 1, 짝수노드 0일 경우 or 홀수노드 0, 짝수노드 1일 경우 -> 홀짝 트리 가능. 
            #  (홀짝노드를 루트로 선택하면, 나머지 역홀짝노드의 leaf가 1 줄어들면서 전부 홀짝노드가 된다)
            if (stats[0] + stats[1]) == 1:
                rlt[0] += 1
            # 역홀수노드 1, 역짝수노드 0일 경우 or 역홀수노드 0, 역짝수노드 1일 경우 -> 역홀짝 트리 가능
            #  역홀짝노드를 root로 선택하면, 나머지 홀짝노드가 전부 역홀짝노드로 변경되기 때문
            if (stats[2] + stats[3]) == 1:
                rlt[1] += 1
    return rlt