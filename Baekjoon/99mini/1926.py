'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1926
카테고리: 그래프
문제 해설
'''

import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

metrix = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

pictures = dict()
count = 0

drow = [0, 0, 1, -1]
dcol = [1, -1, 0, 0]

def dfs(row, col):
    visited[row][col] = True
    pictures[count] += 1

    for dr, dc in zip(drow, dcol):
        nr = row + dr
        nc = col + dc

        if 0 <= nr < n and 0 <= nc < m and metrix[nr][nc] and not visited[nr][nc]:
            dfs(nr, nc)

for row in range(n):
    for col in range(m):
        if metrix[row][col] and not visited[row][col]:
            count += 1
            pictures[count] = 0
            dfs(row, col)

print(count)
print(max(list(pictures[p] for p in pictures)) if count else 0)