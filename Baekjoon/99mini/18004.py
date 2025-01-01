'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/18004
카테고리: BFS
문제 해설
que를 이용하여 bfs.
만약 목표(b)보다 현재(a 혹은 curr)이 작은 경우 b-a(혹은 curr)를 하는 것이 목표로 갈 수 있는 유일한 해결책
'''

import sys
from collections import deque

input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())
    
    if a <= b:
        print(b - a)
        return

    q = deque([(0, a)])
    while q:
        depth, curr = q.popleft()

        if curr == b:
            print(depth)
            return

        if curr > b:
            if curr % 2 == 0:
                q.append((depth + 1, curr // 2))
            else:
                q.append((depth + 1, curr + 1))
        else:
            print(depth + (b - curr))
            return

solution()