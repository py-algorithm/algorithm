'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/17204
카테고리
    - 구현
    - 그래프 이론
    - 그래프 탐색
    - 시뮬레이션
문제 해설
단순 시뮬레이션
'''

import sys

input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())

    people = [ int(input()) for _ in range(n)]

    curr = 0
    res = 0
    for _ in range(n):
        curr = people[curr]
        res += 1

        if curr == k:
            return res
    return -1

print(solution())
