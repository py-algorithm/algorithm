'''
문제 링크:https://www.acmicpc.net/problem/11651
카테고리: 정렬
문제해설: 좌표 정렬하기 2
2차원 평면에 점 n개를 좌표 순으로 정렬하기
1. y좌표 증가하는 순서
2. y좌표 같으면 x좌표 증가하는 순서
'''
import sys

input = sys.stdin.readline

n = int(input())
cor = []

for i in range(n):
  x = list(map(int, input().split()))
  cor.append(x)

cor.sort(key = lambda x : (x[1], x[0]))

for i in cor:
  print(i[0], i[1])