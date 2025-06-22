'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/15786
카테고리: 구현, 그리디 알고리즘, 문자열
'''

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

base_list = list(input().strip())

for _ in range(m):
    test_case = input().strip()

    ptr = 0

    for t in test_case:
        if ptr == n:
            break
        if t == base_list[ptr]:
            ptr += 1

    print(str(ptr == n).lower())