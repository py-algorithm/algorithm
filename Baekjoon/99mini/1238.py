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

# 딕셔너리 초기화
# {1: dict(), 2: dict(), ..., n: dict()}
for i in range(1, n + 1):
    graph[i] = dict()

# graph
# { start_node: { end_node: weight }}
for _ in range(m):
    start, end, weight = map(int, input().split())

    graph[start][end] = weight

distance = [[sys.maxsize] * (n + 1) for _ in range(n+1)]

for i in range(1, n + 1):
    q = []
    # 힙에 (가중치, 노드 번호) 넣기
    heapq.heappush(q, (0, i))

    # 자기자신은 0으로 초기화
    distance[i][i] = 0

    while q:
        dist, curr = heapq.heappop(q)

        # distance에 기록된 가중치가 새로운 가중치보다 작으면 스킵
        if distance[i][curr] < dist:
            continue

        # 현재 노드와 연결된 노드 탐색
        for g in graph[curr]:
            node = g
            weight = graph[curr][g]

            # 현재 가중치 + 새로운 노드의 가중치 < distance에 기록된 가중치
            # distance의 가중치 갱신
            # 힙에 넣기
            if dist + weight < distance[i][node]:
                distance[i][node] = dist + weight
                heapq.heappush(q, (dist + weight, node))

# i -> x, x -> i 두 방향의 가중치의 합이 가장 큰 값 반환
print(max(list(distance[i][x] + distance[x][i] for i in range(1, n+1))))
