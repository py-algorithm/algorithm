'''
작성자: 99mini
문제 링크:https://www.acmicpc.net/problem/2206
카테고리: 그래프 이론, 그래프 탐색, 너비 우선 탐색
문제해설: 
BFS로 탐색하다가 벽을 만나면 벽 방문표시
'''

n, m = map(int, input().split())

tile = [input() for _ in range(n)]

visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]

drow = [0, 0, 1, -1]
dcol = [1, -1, 0, 0]

for col in tile:
  for row in col:
    print(row)