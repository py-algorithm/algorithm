'''
문제 링크:https://www.acmicpc.net/problem/11650
카테고리: 정렬
문제해설: 좌표 정렬하기
2차원 평면에 점 n개를 좌표 순으로 정렬하기
1. x좌표 증가하는 순서
2. x좌표 같으면 y좌표 증가하는 순서


'''
import sys

input = sys.stdin.readline

n = int(input())

cor = []

for i in range(n):
  x, y = map(int, input().split())
  cor.append([x, y])
#[[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]

for i in range(n):
  for j in range(n):
    if cor[i][0] != cor [j][0]:
      cor.sort(key = lambda x : x[0])
    else:
      cor.sort(key = lambda x : x[1])

for i in cor:
  print(i[0], i[1])



