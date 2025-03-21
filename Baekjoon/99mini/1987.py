'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1987
카테고리
    - 그래프 이론
    - 그래프 탐색
    - 깊이 우선 탐색
    - 백트래킹
문제 해설
'''

import sys

input = sys.stdin.readline

r, c = map(int, input().split())

grid = [input() for _ in range(r)]

visited = [False for _ in range(ord('Z') - ord('A') + 1)]

dn = [
    [1,0],
    [-1,0],
    [0,1],
    [0,-1]
]

def is_boundary(row, col):
    return 0 <= row < r and 0 <= col < c

def solution():
    global ret
    ret = 0

    def dfs(row, col, depth):
        global ret
        ret = max(ret, depth)

        visited[ord(grid[row][col]) - ord('A')] = True

        for (dr, dc) in dn:
            next_row, next_col = row + dr, col + dc

            if not is_boundary(next_row, next_col):
                continue
            
            current_value = grid[next_row][next_col]

            if not visited[ord(current_value) - ord('A')]:
                dfs(next_row, next_col, depth + 1)
                visited[ord(current_value) - ord('A')] = False

    dfs(0, 0, 1)

    return ret

print(solution())