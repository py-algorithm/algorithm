'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/14940
카테고리: BFS
문제해설: 
시작 지점을 기분으로 BFS 시행
'''

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = []
start = [0, 0]

for i in range(n):
    row = list(map(int, input().split()))
    for idx, item in enumerate(row):
        if item == 2:
            start = [i, idx]
    board.append(row)

visited = [[-1 if board[i][j] == 1 else 0 for j in range(m)] for i in range(n)]

visited[start[0]][start[1]] = 0

que = deque([(start[0], start[1])])

while que:
    x, y = que.popleft()
    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        nx = x + dx
        ny = y + dy

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if visited[nx][ny] <= 0 and board[nx][ny] == 1:
            que.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

for row in visited:
    print(*row, sep=' ')
