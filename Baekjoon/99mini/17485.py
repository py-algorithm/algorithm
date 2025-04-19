'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/17485
카테고리
    - 다이나믹 프로그래밍
문제 해설
3차원 배열을 이용하여 이전 경로 저장
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # row, col 2 <= n, m <= 100

matrix = list(list(map(int, input().split())) for _ in range(n))
dp = [
        [
            [matrix[j][i] if j == 0 else sys.maxsize if i == 0 or i == m- 1 else (100 * n + 1) for _ in range(3)] for i in range(m) # ~로 부터 | 0: 왼쪽 위 1: 가운데 2: 오른쪽 위 
        ] for j in range(n)
    ]

for row in range(1, n):
    for col in range(m):
        if col - 1 >= 0:
            dp[row][col][0] = min(dp[row - 1][col - 1][1], dp[row - 1][col - 1][2]) + matrix[row][col]

        dp[row][col][1] = min(dp[row - 1][col][0], dp[row - 1][col][2]) + matrix[row][col]
        
        if col + 1 < m:
            dp[row][col][2] = min(dp[row - 1][col + 1][0], dp[row - 1][col + 1][1]) + matrix[row][col]

print(min(min(dp[-1], key=lambda x: min(x))))