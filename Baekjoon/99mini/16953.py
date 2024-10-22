'''
작성자: 99mini
문제 링크: https://www.acmicpc.net/problem/16953
카테고리: 그래프 이론, 그리디 알고리즘, 그래프 탐색, 너비 우선 탐색
문제 해설
- bfs 하여 두 가지 연산을 모두 수행 후 큐에 넣는다
- b 보다 큰 경우 큐에 넣지 않는다연산을 수행하지 않는다
'''

import sys

input = sys.stdin.readline

a, b = map(int, input().split())

def solution(a, b):
  queue = [(a, 1)]

  while queue:
    value, step = queue.pop(0)

    if value == b:
      return step

    multi_value = value * 2
    append_value = value * 10 + 1

    if multi_value <= b:
      queue.append((multi_value, step + 1))

    if append_value <= b:
      queue.append((append_value, step + 1))
  
  return -1

print(solution(a, b))