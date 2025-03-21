'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/1660
카테고리
- 다이나믹 프로그래밍

문제 해설
정사면체의 누적합을 배열로 관리
'''

import sys

input = sys.stdin.readline

MAX = sys.maxsize

n = int(input())

balls = []
b = 0
i = 1
while b < n:
    b += (i * (i + 1)) // 2 # 정사면체에 필요한 포탄의 개수. 1, 4, 10, 20
    balls.append(b)
    i+=1

dp = [MAX]*(n+1)

for i in range(1, n+1):
    for b in balls:
        if b == i:
            dp[i] = 1
        if b >= i:
            break
        dp[i] = min(dp[i], 1 + dp[i - b])
print(dp[n])
