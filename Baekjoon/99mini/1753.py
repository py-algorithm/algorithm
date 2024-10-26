'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1753
카테고리: 그래프, 다익스트라
문제해설: 
'''

import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())

k = int(input())

graph=[[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, input().split())

    graph[a].append((b, w))

distance = [sys.maxsize] * (v + 1)
distance[k] = 0

que = [(0, k)]

while que:
    weight, node = heapq.heappop(que)

    if weight > distance[node]:
        continue
    
    for g in graph[node]:
        
        new_weight = g[1] + weight

        if distance[g[0]] > new_weight:
            distance[g[0]] = new_weight
            heapq.heappush(que, (new_weight, g[0]))

print(*("INF" if distance[i] == sys.maxsize else distance[i] for i in range(1, v+1)), sep="\n")