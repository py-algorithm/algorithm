'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2508
카테고리: 구현, 브루트포스 알고리즘
'''

import sys

input = sys.stdin.readline

def next_ptr(r_ptr, c_ptr, delta = 1):
    r_ptr_new = r_ptr
    c_ptr_new = c_ptr

    if c_ptr == c - delta:
        c_ptr_new = 0
        r_ptr_new += delta
    else:
        c_ptr_new += delta

    return (r_ptr_new, c_ptr_new)

t = int(input())

for _ in range(t):
    _ = input()
    r, c = map(int, input().split())

    box = [list(input().strip()) for _ in range(r)]

    r_ptr = 0
    c_ptr = 0

    ret = 0

    while r_ptr < r and c_ptr < c:
        curr = box[r_ptr][c_ptr]

        if curr == ">" and c_ptr + 2 < c:
            if box[r_ptr][c_ptr + 1] == "o" and box[r_ptr][c_ptr + 2] == "<":
                ret += 1

        elif curr == "v" and r_ptr + 2 < r:
            if box[r_ptr + 1][c_ptr] == "o" and box[r_ptr + 2][c_ptr] == "^":
                ret += 1

        r_ptr, c_ptr = next_ptr(r_ptr, c_ptr)

    print(ret)