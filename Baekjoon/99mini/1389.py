'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1389
카테고리: 그래프, 플로이드 와샬
문제 해설:
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[sys.maxsize] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a][b] = 1
    graph[b][a] = 1

distance = graph.copy()

# k: 거처가는 노드
for k in range(1, n+1):
    distance[k][k] = 0 
    # i: 시작 노드
    for i in range(1, n+1):
        # j: 끝 노드
        for j in range(1, n + 1):
            # i -> k + k -> j 와 i -> j 비교
            distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])

sum_of_d = sys.maxsize

for i in range(1, n + 1):
    curr_sum_of_d = sum(distance[i][1:])

    if sum_of_d > curr_sum_of_d:
        sum_of_d = curr_sum_of_d
        result = i

print(result)