'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1260
카테고리: bfs, dfs
문제해설
'''

from collections import deque

dfs_result = []
bfs_result = []

def dfs(start):
    visited[start] = True
    dfs_result.append(start)

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        bfs_result.append(v)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

visited = [False] * (N + 1)
dfs(V)
print(*dfs_result, sep=" ")

visited = [False] * (N + 1)
bfs(V)
print(*bfs_result, sep=" ")