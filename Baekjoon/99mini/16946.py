'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/16946
카테고리
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

문제 해설
'''

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
tiles = [input().strip() for _ in range(n)]

def is_boundary(row, col) -> bool:
    return row < n and row >= 0 and col < m and col >= 0

def bfs(graph: list[str], row: int, col: int):
    
    dn = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]

    visited = set([(row, col)])
    q = deque([(row, col)])

    while q:
        curr_row, curr_col = q.popleft()

        for delta_row, delta_col in dn:
            next_row = curr_row + delta_row
            next_col = curr_col + delta_col

            if  is_boundary(next_row, next_col) and \
                not (next_row, next_col) in visited and \
                graph[next_row][next_col] == "0" or (next_row == row and next_col == col):
                """
                맵의 경계에 존재
                방문하지 않음
                벽이 아니거나, 최초 진입 지점인 경우 BFS 진행
                """
                visited.add((next_row, next_col))

                q.append((next_row, next_col))

    return len(visited) % 10

for row in range(n):
    for col in range(m):
        if tiles[row][col] == "1":
            print(bfs(tiles, row, col), end="")
        else:
            print("0", end="")
    print()
