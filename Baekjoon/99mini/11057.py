'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/11057
카테고리: 다이나믹 프로그래밍
문제 해설:

dp[N][10]

n   0   1   2   3   4   5   6   7   8   9
1   1   1   1   1   1   1   1   1   1   1
2   1   2   3   ...                     10
3   1   3   6   ...

'''

import sys

input = sys.stdin.readline

n = int(input())

dp = [[1 if i == 0 or j == 0 else 0 for j in range(10)] for i in range(n)]

for i in range(1, n):
    suffix_sum = [0] * 10
    suffix_sum[0] = 1

    for j in range(1, 10):
        suffix_sum[j] = suffix_sum[j-1] + dp[i - 1][j]
        dp[i][j] = suffix_sum[j]

print(sum(dp[n-1]) % 10007)