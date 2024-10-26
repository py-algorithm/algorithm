'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1916
카테고리: 그래프, 다익스트라
문제 해설:
다익스트라
단방향 그래프

a를 출발하는 다익스트라 알고리즘 수행

* 이미 경로가 있는 경우 최소 비용 경로를 택한다.
'''

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = dict()

for i in range(1, n+1):
    graph[i] = dict()

for _ in range(m):
    a, b, w = map(int, input().split())

    # 이미 경로가 있다면 최소 비용 경로만 취한다. 
    if b in graph[a]:
        graph[a][b] = min(w, graph[a][b])
    else:
        graph[a][b] = w

a, b = map(int, input().split())

distance = [sys.maxsize] * (n + 1)
distance[a] = 0

que = []
heapq.heappush(que, (0, a))

while que:
    w, node = heapq.heappop(que)

    if distance[node] < w:
        continue

    for new_node in graph[node]:
        new_weight = w + graph[node][new_node]

        if distance[new_node] > new_weight:
            distance[new_node] = new_weight
            heapq.heappush(que, (new_weight, new_node))

print(distance[b])