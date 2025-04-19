'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/24913
카테고리
    - 수학
    - 구현
문제 해설
'''

import sys

input = sys.stdin.readline

n, q = map(int, input().split())

candidate = dict()

for i in range(1, n + 2):
    candidate[i] = 0

total = 0
max_other = -1

for _ in range(q):
    op, x, y = map(int, input().split())

    if op == 1:
        candidate[y] += x

        if y != (n + 1):
            total += x
            max_other = max(max_other, candidate[y])
    else:
        predict_me = candidate[n + 1] + x

        print("YES" if predict_me > max_other and (predict_me - 1) * n >= total + y else "NO")