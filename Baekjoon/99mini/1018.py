'''
작성자: 99mmini
문제 링크: https://www.acmicpc.net/problem/1018
카테고리: 완전 탐색
문제 해설:
8x8을 완전 탐색
(0, 0)이 B로 시작하는 경우와 W로 시작하는 경우를 나눠서 해결
'''

import sys

N, M = map(int, input().split())

board = [input() for _ in range(N)]

ret = sys.maxsize

for s_i in range(0, N-7):
    for s_j in range(0, M-7):
        w = 0
        b = 0
        for i in range(s_i, s_i + 8):
            for j in range(s_j, s_j + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] == 'W':
                        b += 1
                    else:
                        w += 1
                else:
                    if board[i][j] == 'B':
                        b += 1
                    else:
                        w += 1
        ret = min(ret, w, b)

print(ret)