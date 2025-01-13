'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/2887
카테고리
- 그래프 이론
- 정렬
- 최소 스패닝 트리

문제 해설
'''

import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

coordinate = list(tuple(map(int, input().split())) for _ in range(n))

parent = [i for i in range(n + 1)]

'''
(a, b, weight)
'''
graph: list[tuple[int, int, int]] = []

for i in range(n):
    lhs = coordinate[i]
    for j in range(i + 1, n):
        rhs = coordinate[j]
        graph.append((
            i, 
            j, 
            min(
                abs(lhs[0] - rhs[0]),
                abs(lhs[1] - rhs[1]),
                abs(lhs[2] - rhs[2])
            )
        ))

graph.sort(key=lambda x: x[-1])

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

        if edge_cnt == n - 1:
            break

print(ret)