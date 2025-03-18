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

visited = [[0 for _ in range(m)] for _ in range(n)]
result = visited[::]

dn = [
        [0, 1],
        [0, -1],
        [1, 0],
        [-1, 0]
    ]

def is_boundary(row, col) -> bool:
    return row < n and row >= 0 and col < m and col >= 0

def bfs(graph: list[str], row: int, col: int):
    visited_set = set([(row, col)])
    q = deque([(row, col)])

    while q:
        curr_row, curr_col = q.popleft()

        for delta_row, delta_col in dn:
            next_row = curr_row + delta_row
            next_col = curr_col + delta_col

            if  is_boundary(next_row, next_col) and \
                not (next_row, next_col) in visited_set and \
                graph[next_row][next_col] == "0":
                """
                맵의 경계에 존재
                방문하지 않음
                벽이 아니거나, 최초 진입 지점인 경우 BFS 진행
                """
                visited_set.add((next_row, next_col))

                q.append((next_row, next_col))
    
    for v in visited_set:
        v_row, v_col = v

        visited[v_row][v_col] = len(visited_set)
        

def calc_bfs(row: int, col: int):

    ret = 1

    for delta_row, delta_col in dn:
        next_row = row + delta_row
        next_col = col + delta_col

        if  is_boundary(next_row, next_col) and visited[next_row][next_col]:
            """
            맵의 경계에 존재
            visited > 0
            """
            ret += visited[next_row][next_col]

    return ret % 10
    

for row in range(n):
    for col in range(m):
        if not visited[row][col] and tiles[row][col] == "0":
            bfs(tiles, row, col)

for row in range(n):
    for col in range(m):
        if tiles[row][col] == "1":
            print(calc_bfs(row, col), end="")
        else:
            print("0", end="")
    print()