'''
문제 링크:https://www.acmicpc.net/problem/11650
카테고리: 정렬
문제해설: 좌표 정렬하기
2차원 평면에 점 n개를 좌표 순으로 정렬하기
1. x좌표 증가하는 순서
2. x좌표 같으면 y좌표 증가하는 순서

for문 2개->시간 초과
퀵소트 or 머지소트->시간 복잡도 최악이어도(nlogn) or 내장 함수
'''
import sys

input = sys.stdin.readline

n = int(input())

cor = []

for i in range(n):
  x = list(map(int, input().split()))
  cor.append(x)
#[[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]

cor.sort(key = lambda x : (x[0], x[1]))

for i in cor:
  print(i[0], i[1])



