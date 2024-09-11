'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2206
카테고리: 그래프 이론, 그래프 탐색, 너비 우선 탐색
문제해설: [WIP]
'''

n, m = map(int, input().split())

tile = [input() for _ in range(n)]

for col in tile:
  for row in col:
    print(row)