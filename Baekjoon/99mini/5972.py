'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/5972
카테고리
- 그래프 이론
- 최단 경로
- 데이크스트라
문제해설:
1을 시작으로 n까지의 최소 비용을 구하는 최소 경로 알고리즘 계산
중복된 간선이 있는 경우 최소비용으로 세팅
'''

import sys
import heapq

n, m = map(int ,input().split())

graph: dict[int, dict[int, int]] = dict()

visited = [0, 0] + [sys.maxsize] * (n - 1)

for _ in range(m):
    a, b, cost = map(int ,input().split())

    if a not in graph:
        graph[a] = dict({
            b: cost
        })
    else:
        if b in graph[a]:
            graph[a][b] = min(cost, graph[a][b])
        else:
            graph[a][b] = cost
    if b not in graph:
        graph[b] = dict({
            a: cost
        })
    else:
        if a in graph[b]:
            graph[b][a] = min(cost, graph[b][a])
        else:
            graph[b][a] = cost

q = []
heapq.heappush(q, (0, 1))

while q:
    cost, vertex = heapq.heappop(q)

    if visited[vertex] < cost:
        continue

    for next_vertex in graph[vertex].keys():
        next_distance = cost + graph[vertex][next_vertex]

        if next_distance < visited[next_vertex]:
            visited[next_vertex] = next_distance
            heapq.heappush(q, (next_distance, next_vertex))

print(visited[n])