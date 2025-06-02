'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/20206
카테고리: 수학, 기하학
문제 해설
'''

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())

upper_count = 0
under_count = 0

for (x, y) in [
    (x1, y1),
    (x1, y2),
    (x2, y1),
    (x2, y2)
]:
    position = a*x + b*y

    if position >= -c:
        upper_count += 1
    if position <= -c:
        under_count += 1

if upper_count == 4 or under_count == 4:
    print("Lucky")
else:
    print("Poor")