'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2583
카테고리: 그래프 탐색
문제해설
'''

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

m, n, k = map(int, input().split())

grid = [[False] * n for _ in range(m)]

for _ in range(k):
    bottom_left_x, bottom_left_y, top_right_x, top_right_y = map(int, input().split())

    for x in range(bottom_left_x, top_right_x):
        for y in range(bottom_left_y, top_right_y):
            grid[y][x] = True

count = 0

area = dict()

visited = [[False] * n for _ in range(m)]

delta_x_unit = [0, 0, 1, -1]
delta_y_unit = [1, -1, 0, 0]

def dfs(x, y):
    visited[y][x] = True
    area[count] += 1

    for dx, dy in zip(delta_x_unit, delta_y_unit):
        cx = x + dx
        cy = y + dy

        if ( cx >= 0 and cx < n ) and ( cy >= 0 and cy < m ) and not visited[cy][cx] and not grid[cy][cx]:
            dfs(cx, cy)


for x in range(n):
    for y in range(m):
        if not visited[y][x] and not grid[y][x]:
            count += 1
            area[count] = 0
            dfs(x, y)

print(count)
print(*sorted(list(area[a] for a in area)))

