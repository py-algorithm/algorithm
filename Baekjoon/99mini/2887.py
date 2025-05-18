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

graph: dict[int, dict[int, int]] = dict()

for i in range(n):
    graph[i + 1] = dict()


for i in range(1, n + 1):
    lhs = coordinate[i - 1]

    for j in range(i + 1, n + 1):
        rhs = coordinate[j - 1]
        
        weight = min(
            abs(lhs[0] - rhs[0]),
            abs(lhs[1] - rhs[1]),
            abs(lhs[2] - rhs[2])
        )

        if j not in graph[i]:
            graph[i][j] = weight
        else:
            graph[i][j] = min(weight, graph[i][j])
        if i not in graph[j]:
            graph[j][i] = weight
        else:
            graph[j][i] = min(weight, graph[j][i])


visited = [False for _ in range(n + 1)]

print(graph)
