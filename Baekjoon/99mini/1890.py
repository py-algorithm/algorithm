'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/1890
카테고리: 다이나믹 프로그래밍, dp
문제해설: 
'''

import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if not dp[x][y] or not graph[x][y]:
            continue
        nx = x + graph[x][y]
        ny = y + graph[x][y]

        if nx < n:
            dp[nx][y] += dp[x][y]
        if ny < n:
            dp[x][ny] += dp[x][y]

print(dp[-1][-1])