'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1197
카테고리
- 그래프 이론
- 최소 스패닝 트리

문제 해설

1. 유니온 파인드 알고리즘
    - find_root
    - union_root
2. 크루스칼 알로리즘
가중치를 오름차순으로 정렬하고 유니온 파인드 알고리즘을 통해 사이클이 발생하지 않도록 간선 신장
'''

import sys

sys.getrecursionlimit(10**6)

v, e = map(int, input().split())

parent = [i for i in range(v + 1)]

graph = []

for _ in range(e):
    a, b, c = map(int, input().split())

    graph.append((a, b, c))

graph.sort(key = lambda x: x[2])

def find_parent(edge: int) -> int:
    if parent[edge] == edge:
        return edge
    parent[edge] = find_parent(parent[edge])
    return parent[edge]

def union(a: int, b: int) -> None:
    lhs = find_parent(a)
    rhs = find_parent(b)

    if lhs < rhs:
        parent[rhs] = lhs
    else:
        parent[lhs] = rhs

ret = 0
edge_cnt = 0

for a, b, c in graph:
    if find_parent(a) != find_parent(b):
        union(a, b)
        ret += c
        edge_cnt += 1

        if edge_cnt == v - 1:
            break

print(ret)