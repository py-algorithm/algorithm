'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/31946
카테고리
    - BFS
문제 해설
멘허튼 거리 이동을 위하여 1, -1 곱하여 이동
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

field = [list(map(int, input().split())) for _ in range(n)]

start = field[0][0]

x = int(input())

def solution():
    if start != field[-1][-1]:
        return 'DEAD'

    visitied = [[False for _ in range(m)] for _ in range(n)]
    visitied[0][0] = True

    q = deque([(0,0)])

    while q:
        row, col = q.popleft()

        for drow in range(x + 1):
            for dcol in range(x + 1 - drow):
                for (direction_row, direction_col) in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    next_row = direction_row * drow + row
                    next_col = direction_col * dcol + col

                    if not (0 <= next_row < n and 0 <= next_col < m):
                        continue

                    if field[next_row][next_col] != start or visitied[next_row][next_col]:
                        continue

                    q.append((next_row, next_col))
                    visitied[next_row][next_col] = True
    
    return 'ALIVE' if visitied[-1][-1] else 'DEAD'

print(solution())