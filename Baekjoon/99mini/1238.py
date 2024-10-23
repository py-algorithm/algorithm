'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1238
카테고리: 다익스트라
문제해설: 
모든 시작 노드에서 다익스트라 실행

max(distance[i][x] + distance[x][i]) i = 1..n
'''

import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = dict()

for i in range(1, n + 1):
    graph[i] = dict()

for _ in range(m):
    start, end, weight = map(int, input().split())

    graph[start][end] = weight

distance = [[sys.maxsize] * (n + 1) for _ in range(n+1)]

for i in range(1, n + 1):
    q = []
    heapq.heappush(q, (0, i))

    distance[i][i] = 0

    while q:
        dist, curr = heapq.heappop(q)

        if distance[i][curr] < dist:
            continue

        for g in graph[curr]:
            node = g
            weight = graph[curr][g]

            if dist + weight < distance[i][node]:
                distance[i][node] = dist + weight
                heapq.heappush(q, (dist + weight, node))

print(max(list(distance[i][x] + distance[x][i] for i in range(1, n+1))))
