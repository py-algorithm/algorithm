'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/16724
카테고리
    -  자료 구조
    - 그래프 이론
    - 그래프 탐색
    - 깊이 우선 탐색
    - 분리 집합
문제 해설
사이클을 찾아 결과값에 더해주는 방식으로 해결
visitied를 시작 좌표(부모 좌표)로 초기화하고, 시작점과 현재지점의 visitied값이 같은 경우 사이클로 판단
'''

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split()) # n: row, m: col

grid = [input().strip() for _ in range(n)]

ret = 0

visited = [[(row, col) for col in range(m)] for row in range(n)]

for row in range(n):
    for col in range(m):
        if visited[row][col] != (row, col):
            continue

        q = deque([])

        direction = grid[row][col]

        if direction == "U":
            q.append((row - 1, col))
        elif direction == "D":
            q.append((row + 1, col))
        elif direction == "L":
            q.append((row, col - 1))
        else: # R
            q.append((row, col + 1))
            
        while q:
            curr_row, curr_col = q.popleft()

            if visited[row][col] == visited[curr_row][curr_col]:
                ret += 1
                break

            if visited[curr_row][curr_col] != (curr_row, curr_col):
                continue

            direction = grid[curr_row][curr_col]

            visited[curr_row][curr_col] = visited[row][col]

            if direction == "U":
                q.append((curr_row - 1, curr_col))
            elif direction == "D":
                q.append((curr_row + 1, curr_col))
            elif direction == "L":
                q.append((curr_row, curr_col - 1))
            else: # R
                q.append((curr_row, curr_col + 1))

print(ret)