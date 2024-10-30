'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2293
카테고리: 다아니믹 프로그래밍, dp
문제해설
테스트 케이스
3 10
1
2
5

2를 만드는 방법
dp[2] + dp[2 - coin]
* dp[2 - coin]: dp에서 coin 만큼 전에서 만들 수 있는 경우의 수
'''

import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

dp = [1] + [0] * k

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]
print(dp[k])