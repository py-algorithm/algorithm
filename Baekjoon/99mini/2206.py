'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2206
카테고리: 그래프 탐색
문제해설
3차원을 이용하여 벽을 뚫을 경우 판단
'''

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = [list(map(str, input().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx_list = [0,0,1,-1]
dy_list = [1,-1,0,0]


def bfs():
    que = deque()
    que.append((0, 0, 0))

    while que:
        x, y, z = que.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][z]

        for dx, dy in zip(dx_list, dy_list):
            nx = dx + x
            ny = dy + y

            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if graph[nx][ny] == "1" and z == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    que.append((nx, ny, 1))
                
                elif graph[nx][ny] == "0" and not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    que.append((nx, ny, z))

    return -1

print(bfs())