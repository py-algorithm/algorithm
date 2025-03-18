'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/10571
카테고리
    - 다이나믹 프로그래밍
문제 해설
    - 가장 긴 증가하는 부분 수열
'''

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    diamond_list = list(
        list(map(float, input().split())) for _ in range(n)
    )

    dp = [0 for _ in range(n)]

    for i in range(n):
        dp[i] = 1
        head_w, head_c = diamond_list[i]

        for j in range(i):
            tail_w, tail_c = diamond_list[j]

            if head_w > tail_w and head_c < tail_c:
                dp[i] = max(dp[j] + 1, dp[i])
    
    print(max(dp))