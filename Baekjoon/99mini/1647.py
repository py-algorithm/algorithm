'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1647
카테고리
- 그래프 이론
- 최소 스패닝 트리

문제 해설
ref: https://www.acmicpc.net/problem/1197
최소신장 트리에서 마지막 간선(최소 신장 트리에서 가중치가 가장 큰 간선)을 제외하고 최소 신장 트리 생성
'''

import sys

sys.setrecursionlimit(10**6)

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
        if edge_cnt == v - 2:
            break
        ret += c
        edge_cnt += 1

print(ret)