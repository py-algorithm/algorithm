'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2252
카테고리
- 그래프 이론
- 방향 비순환 그래프
- 위상 정렬

문제해설
위상 정렬
'''

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph: dict[int, set[int]] = {}
'''
1-indexed
'''

in_degree_list: list[int] = [0 for _ in range(n + 1)]
'''
1-indexed
'''

for i in range(n):
    graph[i + 1] = set([])

for _ in range(m):
    pre, post = map(int, input().split())

    # 단방향 그래프 진출 간선 기록
    graph[pre].add(post)

    # 진입 차수 기록
    in_degree_list[post] += 1

que: deque[int] = deque([])

for i in range(n):
    # 진입 차수가 0인 경우 큐에 삽입
    if not in_degree_list[i + 1]:
        que.append(i + 1)

ans = []

while que:
    curr = que.popleft()
    ans.append(str(curr))

    for i in graph[curr]:
        in_degree_list[i] -= 1

        if in_degree_list[i] == 0:
            que.append(i)

print(" ".join(ans))