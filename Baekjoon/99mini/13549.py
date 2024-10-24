'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/13549
카테고리: BFS
문제해설: 
너비 우선 탐색. 바운더리를 넘어갈 경우 continue
'''

import sys
from collections import deque 

input = sys.stdin.readline

n, k = map(int, input().split())

que = deque([(n, 0)])

visisted = [False] * 100_001

while que:
    curr, t = que.popleft()
    visisted[curr] = True

    if curr == k:
        print(t)
        break
    
    for nx in (curr * 2, curr - 1, curr + 1):
        if nx > 100_000 or nx < 0:
            continue
        if visisted[nx]:
            continue
        if nx == curr * 2:
            que.append((nx, t))
        else:
            que.append((nx, t + 1))